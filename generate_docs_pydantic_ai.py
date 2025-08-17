import os
from parser import endpoints
from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel
from pydantic_ai import Agent
import json

# Load environment variables
load_dotenv()

# Keep your existing Pydantic models - they work perfectly!
class ResponseContent(BaseModel):
    example: dict

class Response(BaseModel):
    description: str
    content: ResponseContent

class Method(BaseModel):
    operationId: str
    description: str
    responses: List[Response]

class OpenAPIPath(BaseModel):
    path: str
    method: Method

class OpenAPISpec(BaseModel):
    paths: List[OpenAPIPath]

# Replace Hugging Face client with Pydantic AI agent
def setup_pydantic_ai_agent():
    """Initialize Pydantic AI agent with gpt-3.5-turbo-0125"""
    
    # Validate API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("❌ OPENAI_API_KEY not found in environment variables. Please add it to your .env file.")
    
    print(f"🔑 OpenAI API Key loaded: {api_key[:8]}***")
    
    # Create agent with same functionality as your HF client
    agent = Agent(
        model='openai:gpt-3.5-turbo-0125',
        system_prompt="""
        You are an expert OpenAPI 3.0 specification generator.
        
        Your task is to generate OpenAPI path fragments for Flask endpoints.
        
        Guidelines:
        - Analyze the provided Flask endpoint code
        - Generate accurate OpenAPI 3.0 documentation
        - Include realistic examples and descriptions
        - Create proper HTTP status codes based on the endpoint logic
        - Include curl command examples in descriptions
        - Always return valid JSON in the exact format requested
        - DO NOT include any additional text or markdown outside the JSON
        
        Focus on creating accurate, useful documentation that developers can immediately use.
        """
    )
    
    return agent

# Replace your hf_query function with pydantic_ai_query
def pydantic_ai_query(agent, prompt):
    """Query Pydantic AI agent - direct replacement for hf_query function"""
    
    try:
        # Run the agent with your existing prompt
        result = agent.run_sync(prompt)
        
        # Extract response text - handle different Pydantic AI response formats
        if hasattr(result, 'data'):
            response_text = result.data
        elif hasattr(result, 'output'):
            response_text = result.output
        else:
            response_text = str(result)
        
        # Clean up response to ensure it's valid JSON
        response_text = response_text.strip()
        
        # Remove any markdown code block markers
        if response_text.startswith('```json'):
            response_text = response_text.replace('```json', '').replace('```', '').strip()
        elif response_text.startswith('```'):
            response_text = response_text.replace('```', '').strip()
        
        # Try to parse as JSON to validate
        try:
            json.loads(response_text)
            return response_text
        except json.JSONDecodeError:
            # If it's not valid JSON, try to extract JSON from response
            import re
            
            # Try different JSON extraction patterns
            json_patterns = [
                r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}',  # Simple nested JSON
                r'(\{.*\})',  # Any text between first { and last }
            ]
            
            for pattern in json_patterns:
                matches = re.findall(pattern, response_text, re.DOTALL)
                for match in matches:
                    try:
                        json.loads(match)
                        return match
                    except json.JSONDecodeError:
                        continue
                        
            raise ValueError("No valid JSON found in AI response")
                
    except Exception as e:
        print(f"⚠️ AI query failed: {e}")
        print(f"🔍 Raw response: {response_text[:200]}..." if 'response_text' in locals() else "No response received")
        # Return a basic fallback structure
        return generate_fallback_response(prompt)

def generate_fallback_response(prompt):
    """Generate fallback response when AI fails - maintains your existing structure"""
    
    # Extract endpoint info from prompt (simple parsing)
    import re
    
    func_match = re.search(r'operationId\*\*: (.+)', prompt)
    method_match = re.search(r'method\*\*: (.+)', prompt)
    path_match = re.search(r'path\*\*: (.+)', prompt)
    
    func_name = func_match.group(1).strip() if func_match else "unknown_function"
    method = method_match.group(1).strip() if method_match else "GET"
    path = path_match.group(1).strip() if path_match else "/unknown"
    
    # Generate basic but valid OpenAPI fragment
    fallback = {
        path: {
            method.lower(): {
                "operationId": func_name,
                "summary": f"{method} {path}",
                "description": f"Endpoint handled by {func_name} function.\n\n**Example curl command:**\n```bash\ncurl -X {method} 'http://localhost:5000{path}'\n```",
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "content": {
                            "application/json": {
                                "example": {"message": "success", "data": "example"}
                            }
                        }
                    }
                }
            }
        }
    }
    
    return json.dumps(fallback)

# Initialize the Pydantic AI agent (replaces your HF client setup)
print("🚀 Initializing Pydantic AI agent...")
agent = setup_pydantic_ai_agent()
print("✅ Pydantic AI agent ready!")

# Your existing logic - minimal changes!
os.makedirs("docs", exist_ok=True)

# Collect all paths first, then write them properly
all_paths = {}

for idx, e in enumerate(endpoints):
    # Your exact same prompt - no changes needed!
    prompt = f"""
            Generate an OpenAPI path fragment for the following endpoint. 
            Return ONLY a JSON object in this EXACT format:
            {{
                "{e['path']}": {{
                    "{e['methods'][0].lower()}": {{
                        "operationId": "{e['func']}",
                        "summary": "Brief description of what this endpoint does",
                        "description": "Detailed description including curl example: curl -X {e['methods'][0]} 'http://localhost:5000{e['path']}'",
                        "responses": {{
                            "200": {{
                                "description": "Successful response",
                                "content": {{
                                    "application/json": {{
                                        "example": {{}}
                                    }}
                                }}
                            }}
                        }}
                    }}
                }}
            }}

            Endpoint details:
            - **Function**: {e['func']}
            - **Method**: {e['methods'][0]}
            - **Path**: {e['path']}
            - **Code**: {e['code']}

            Return ONLY the JSON object. NO other text or markdown.
            """
    
    # Replace hf_query with pydantic_ai_query - only line that changes!
    docs = pydantic_ai_query(agent, prompt)
    print(f"📋 Generated docs for {e['path']}")
    print(docs)
    
    # Parse and merge the path into all_paths
    try:
        parsed_json = json.loads(docs)
        # Merge this path into all_paths
        all_paths.update(parsed_json)
        print(f"✅ Successfully processed {e['path']}")
    except json.JSONDecodeError as json_error:
        print(f"❌ JSON parsing error for {e['path']}: {json_error}")
        print(f"🔄 Using fallback for endpoint {e['path']}")
        # Use fallback and continue
        fallback_docs = generate_fallback_response(prompt)
        fallback_json = json.loads(fallback_docs)
        all_paths.update(fallback_json)

# Now write the complete OpenAPI spec
with open("docs/openapi_pydantic_ai.json", "w") as out:
    complete_spec = {
        "openapi": "3.0.0",
        "info": {
            "title": "Flask API Documentation",
            "description": "Auto-generated API documentation using Pydantic AI agents",
            "version": "1.0.0"
        },
        "servers": [
            {"url": "http://localhost:5000", "description": "Development server"}
        ],
        "paths": all_paths
    }
    json.dump(complete_spec, out, indent=2)

print("🎉 Successfully wrote docs/openapi_pydantic_ai.json using Pydantic AI!")
print("\n📊 Summary:")
print(f"  • Processed {len(endpoints)} endpoints")
print(f"  • Used model: gpt-3.5-turbo-0125")
print(f"  • Output: docs/openapi_pydantic_ai.json")

# Optional: Create simple Swagger UI HTML for viewing
swagger_html = """<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <title>API Reference - Pydantic AI Generated</title>
  <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist/swagger-ui.css" />
  <style>
    .swagger-ui .topbar { background-color: #1976d2; }
    .custom-header {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white; padding: 20px; text-align: center; margin-bottom: 20px;
    }
    .custom-header h1 { margin: 0; font-size: 2em; }
    .custom-header p { margin: 10px 0 0 0; opacity: 0.9; }
  </style>
</head>
<body>
  <div class="custom-header">
    <h1>🤖 API Documentation</h1>
    <p>Generated with Pydantic AI agents using gpt-3.5-turbo-0125</p>
  </div>
  <div id="swagger-ui"></div>
  <script src="https://unpkg.com/swagger-ui-dist/swagger-ui-bundle.js"></script>
  <script>
    SwaggerUIBundle({
      url: "openapi_pydantic_ai.json",
      dom_id: "#swagger-ui",
      presets: [
        SwaggerUIBundle.presets.apis,
        SwaggerUIBundle.presets.standalone
      ],
      layout: "StandaloneLayout"
    });
  </script>
</body>
</html>"""

with open("docs/index_pydantic_ai.html", "w") as f:
    f.write(swagger_html)

print("🌐 Bonus: Created docs/index_pydantic_ai.html for Swagger UI!")
print("📱 Open docs/index_pydantic_ai.html in your browser to view the documentation")
