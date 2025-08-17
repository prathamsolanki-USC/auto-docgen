import os
from parser import endpoints
from huggingface_hub import InferenceClient
from typing import List
from pydantic import BaseModel
import json
import pprint

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


client = InferenceClient(
    model = "openai/gpt-oss-120b",
)

def hf_query(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        tools=[
        {
            "type": "function",
            "function": {
                "name": "GenerateOpenAPIFragment",
                "description": "Generate an OpenAPI path fragment for the endpoint.",
                "parameters": {
                    "$defs": {
                        "OpenAPIPath": OpenAPIPath.model_json_schema(),
                        "Response": Response.model_json_schema(),
                        "Method": Method.model_json_schema()
                    },
                    "properties": {
                        "paths": {
                            "items": {
                                "$ref": "#/$defs/OpenAPIPath"
                            },
                            "type": "array",
                            "title": "Paths"
                        }
                    },
                    "required": ["paths"],
                    "type": "object"
                }
            }
        }
    ],
    tool_choice={
        "type": "function",
        "function": {"name": "GenerateOpenAPIFragment"},
    }
    )
    if response.choices[0].finish_reason == "stop":
        return response.choices[0].message["content"]
    elif response.choices[0].finish_reason == "tool_calls":     
        return response.choices[0].message["tool_calls"][0]["function"]["arguments"]

os.makedirs("docs", exist_ok=True)
with open("docs/openapi.json", "w") as out:
    out.write("{\n")
    for idx, e in enumerate(endpoints):
        prompt = f"""
                Generate an OpenAPI path fragment for the following endpoint. 
                Only return the **JSON object** in the format:
                "/path": {{}}

                - **operationId**: {e['func']}
                - **method**: {e['methods'][0]}
                - **path**: {e['path']}
                - **code**: {e['code']}

                Include a short description and an example curl command **inside the JSON**.
                DO NOT include any additional text or markdown.
                """
        docs = hf_query(prompt)
        print(docs)
        # Clean and validate the response
        parsed_json = json.loads(docs)
        # validated_output = OpenAPISpec.model_validate(parsed_json)
        
        # Append the valid output
        out.write(docs)
        if idx < len(endpoints) - 1:
            out.write(",\n")  # Avoid trailing comma for the last item
    out.write("\n}\n")  # Close the JSON object
print("wrote docs/openapi.json")





