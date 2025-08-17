# OpenAPI Generator using Hugging Face model (same as test_model.py approach)
import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
import json
from typing import List, Optional

# Load environment variables
load_dotenv('.env')

# Define structured output models using Pydantic
class OpenAPIEndpoint(BaseModel):
    """Model for a single OpenAPI endpoint definition"""
    path: str
    method: str
    operationId: str
    summary: str
    description: str
    responses: dict
    parameters: Optional[List[dict]] = None
    requestBody: Optional[dict] = None

# Create OpenAI client with Hugging Face endpoint (same as test_model.py)
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

def generate_endpoint_docs(endpoint_data):
    """Generate OpenAPI docs for a single endpoint using HF model"""
    print(f"🤖 Generating docs for {endpoint_data['path']}...")
    
    prompt = f"""
    Generate OpenAPI 3.0 JSON for this Flask endpoint:
    
    Function: {endpoint_data['func']}
    Path: {endpoint_data['path']}
    Method: {endpoint_data['methods'][0]}
    Code: {endpoint_data['code']}
    Description: {endpoint_data.get('docstring', 'No description')}
    
    Return ONLY valid JSON in this format:
    {{
        "paths": {{
            "{endpoint_data['path']}": {{
                "{endpoint_data['methods'][0].lower()}": {{
                    "operationId": "{endpoint_data['func']}",
                    "summary": "Short description",
                    "description": "Detailed description",
                    "responses": {{
                        "200": {{
                            "description": "Success response",
                            "content": {{
                                "application/json": {{
                                    "schema": {{
                                        "type": "object"
                                    }}
                                }}
                            }}
                        }}
                    }}
                }}
            }}
        }}
    }}
    """
    
    try:
        # Use same model call as test_model.py
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b:fireworks-ai",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        )
        
        response_content = completion.choices[0].message.content
        print(f"✅ Generated docs for {endpoint_data['path']}")
        return response_content
        
    except Exception as e:
        print(f"❌ Error generating docs: {e}")
        return None

def create_complete_doc(endpoints_data):
    """Create complete OpenAPI document from multiple endpoints"""
    print("📋 Creating complete OpenAPI document...")
    
    # Generate individual endpoint docs
    all_paths = {}
    
    for endpoint in endpoints_data:
        doc_json = generate_endpoint_docs(endpoint)
        if doc_json:
            try:
                # Parse the JSON response
                parsed = json.loads(doc_json)
                # Extract paths and merge
                if 'paths' in parsed:
                    all_paths.update(parsed['paths'])
            except json.JSONDecodeError as e:
                print(f"❌ Failed to parse JSON for {endpoint['path']}: {e}")
    
    # Create complete OpenAPI document
    complete_doc = {
        "openapi": "3.0.0",
        "info": {
            "title": "Flask API Documentation",
            "version": "1.0.0",
            "description": "Auto-generated API documentation using Hugging Face model"
        },
        "paths": all_paths
    }
    
    return complete_doc

def main():
    """Main function to demonstrate HF model usage"""
    print("🎯 Starting Hugging Face OpenAPI Generator\n")
    
    # Sample endpoint data (simulating parser.py output)
    sample_endpoints = [
        {
            'func': 'get_menu',
            'path': '/menu',
            'methods': ['GET'],
            'code': '''@app.route('/menu', methods=['GET'])
def get_menu():
    """Get all menu items"""
    return jsonify([
        {'id': 1, 'name': 'Pizza', 'price': 12.99},
        {'id': 2, 'name': 'Burger', 'price': 8.99}
    ])''',
            'docstring': 'Get all menu items'
        },
        {
            'func': 'add_menu_item',
            'path': '/menu',
            'methods': ['POST'],
            'code': '''@app.route('/menu', methods=['POST'])
def add_menu_item():
    """Add new menu item"""
    data = request.get_json()
    return jsonify({
        'id': 3,
        'name': data['name'],
        'price': data['price']
    }), 201''',
            'docstring': 'Add new menu item'
        }
    ]
    
    # Generate documentation using HF model (same as test_model.py)
    complete_doc = create_complete_doc(sample_endpoints)
    
    # Display results
    print(f"\n🎉 Complete OpenAPI document created!")
    print(f"Title: {complete_doc['info']['title']}")
    print(f"Version: {complete_doc['info']['version']}")
    print(f"Paths: {len(complete_doc['paths'])} endpoints")
    
    # Save to file
    os.makedirs("docs", exist_ok=True)
    with open("docs/hf_openapi.json", "w") as f:
        json.dump(complete_doc, f, indent=2)
    print("💾 Saved to docs/hf_openapi.json")
    
    # Pretty print the result
    print("\n📄 Generated OpenAPI JSON:")
    print(json.dumps(complete_doc, indent=2))

if __name__ == '__main__':
    main()