import ast
import inspect
import os
from openai import OpenAI
from dotenv import load_dotenv
import json
import pprint
# Load environment variables
load_dotenv('.env')

# Simple Menu API
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/menu', methods=['GET'])
def get_menu():
    """Get all menu items"""
    return jsonify([
        {'id': 1, 'name': 'Pizza', 'price': 12.99},
        {'id': 2, 'name': 'Burger', 'price': 8.99},
        {'id': 3, 'name': 'Pasta', 'price': 10.50}
    ])

@app.route('/menu', methods=['POST'])
def add_menu_item():
    """Add new menu item"""
    data = request.get_json()
    return jsonify({
        'id': 4,
        'name': data['name'], 
        'price': data['price']
    }), 201

# AST Parser
def parse_flask_app():
    """Parse Flask app and extract endpoint details"""
    print("🔍 Parsing Flask app...")
    
    import sys
    current_module = sys.modules[__name__]
    source = inspect.getsource(current_module)
    tree = ast.parse(source)
    
    endpoints = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for decorator in node.decorator_list:
                if (isinstance(decorator, ast.Call) and 
                    hasattr(decorator.func, 'attr') and 
                    decorator.func.attr == 'route'):
                    
                    path = decorator.args[0].s
                    methods = ['GET']
                    
                    for keyword in decorator.keywords:
                        if keyword.arg == 'methods':
                            methods = [m.s for m in keyword.value.elts]
                    
                    func_source = inspect.getsource(getattr(current_module, node.name))
                    
                    endpoints.append({
                        'func': node.name,
                        'path': path,
                        'methods': methods,
                        'code': func_source,
                        'docstring': ast.get_docstring(node)
                    })
    
    print(f"✅ Found {len(endpoints)} endpoints")
    return endpoints

def display_endpoints(endpoints):
    """Display parsed endpoints"""
    print("\n📋 Menu API endpoints:")
    for i, ep in enumerate(endpoints, 1):
        print(f"\n🔹 Endpoint {i}:")
        pprint.pprint(ep, indent=2)
        print("-" * 40)

def generate_openapi_for_endpoint(endpoint):
    """Generate OpenAPI for single endpoint"""
    print(f"\n🤖 Generating OpenAPI for {endpoint['path']}...")
    
    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=os.environ["HF_TOKEN"],
    )
    
    prompt = f"""
    Create OpenAPI JSON for this menu API endpoint:
    
    Path: {endpoint['path']}
    Method: {endpoint['methods'][0]}
    Function: {endpoint['func']}
    Description: {endpoint['docstring']}
    
    Return only clean JSON for OpenAPI 3.0 format.
    """
    
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b:fireworks-ai",
        messages=[{"role": "user", "content": prompt}]
    )
    
    print(f"=== {endpoint['methods'][0]} {endpoint['path']} ===")
    print(response.choices[0].message.content)
    return response.choices[0].message.content

def generate_all_openapi(endpoints):
    """Generate OpenAPI for all endpoints"""
    print("\n🚀 Generating OpenAPI for all endpoints...")
    results = []
    
    for endpoint in endpoints:
        result = generate_openapi_for_endpoint(endpoint)
        results.append(result)
    
    return results

def main():
    """Main function - call individual functions"""
    print("🎯 Starting OpenAPI Generator\n")
    
    # Step 1: Parse Flask app
    endpoints = parse_flask_app()
    
    # Step 2: Display what we found
    display_endpoints(endpoints)
    
    # Step 3: Choose what to do
    print("\n🎮 Choose an option:")
    print("1. Generate OpenAPI for first endpoint only")
    print("2. Generate OpenAPI for all endpoints")
    print("3. Just show endpoint details")
    
    choice = input("Enter choice (1/2/3): ")
    
    if choice == "1":
        if endpoints:
            generate_openapi_for_endpoint(endpoints[0])
        else:
            print("No endpoints found!")
    
    elif choice == "2":
        generate_all_openapi(endpoints)
    
    elif choice == "3":
        print("✅ Endpoint details already shown above!")
    
    else:
        print("Invalid choice!")

if __name__ == '__main__':
    main()
