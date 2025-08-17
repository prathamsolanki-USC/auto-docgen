#!/usr/bin/env python3
"""
Swagger UI Server for OpenAPI Documentation

This script serves a Swagger UI interface for the generated OpenAPI specification
using the openapi_pydantic_ai.json file.
"""

import os
import json
from flask import Flask, render_template_string, jsonify, send_from_directory
import webbrowser
import threading
import time

app = Flask(__name__)

# Enhanced Swagger UI HTML template
SWAGGER_UI_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Documentation - Swagger UI</title>
    <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui.css" />
    <link rel="icon" type="image/png" href="https://unpkg.com/swagger-ui-dist@5.9.0/favicon-32x32.png" sizes="32x32" />
    <style>
        html {
            box-sizing: border-box;
            overflow: -moz-scrollbars-vertical;
            overflow-y: scroll;
        }
        *, *:before, *:after {
            box-sizing: inherit;
        }
        body {
            margin: 0;
            background: #fafafa;
        }
        .swagger-ui .topbar {
            background-color: #1976d2;
        }
        .custom-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            text-align: center;
            margin-bottom: 20px;
        }
        .custom-header h1 {
            margin: 0;
            font-size: 2.5em;
            font-weight: 300;
        }
        .custom-header p {
            margin: 10px 0 0 0;
            font-size: 1.2em;
            opacity: 0.9;
        }
        .info-bar {
            background: #e3f2fd;
            border-left: 4px solid #2196f3;
            padding: 15px;
            margin: 20px;
            border-radius: 4px;
        }
        .info-bar h3 {
            margin-top: 0;
            color: #1976d2;
        }
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin: 20px;
        }
        .feature-card {
            background: white;
            padding: 15px;
            border-radius: 6px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            border-left: 3px solid #4caf50;
        }
        .feature-card h4 {
            margin-top: 0;
            color: #2e7d32;
            font-size: 1.1em;
        }
        .feature-card p {
            margin-bottom: 0;
            font-size: 0.9em;
            color: #666;
        }
        .server-info {
            background: #fff3e0;
            border-left: 4px solid #ff9800;
            padding: 15px;
            margin: 20px;
            border-radius: 4px;
        }
        .server-info h3 {
            margin-top: 0;
            color: #f57c00;
        }
        .status-indicator {
            display: inline-block;
            width: 8px;
            height: 8px;
            background-color: #4caf50;
            border-radius: 50%;
            margin-right: 8px;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="custom-header">
        <h1>🚀 API Documentation</h1>
        <p>Generated with Pydantic AI agents using gpt-3.5-turbo-0125</p>
        <p><span class="status-indicator"></span>Hosted on {{ host_url }}</p>
    </div>
    
    <div class="server-info">
        <h3>📡 Server Information</h3>
        <p><strong>Swagger UI URL:</strong> <a href="{{ host_url }}" target="_blank">{{ host_url }}</a></p>
        <p><strong>OpenAPI Spec URL:</strong> <a href="{{ host_url }}/api/openapi.json" target="_blank">{{ host_url }}/api/openapi.json</a></p>
        <p><strong>Status:</strong> <span style="color: #4caf50;">✅ Live and Running</span></p>
    </div>
    
    <div class="features-grid">
        <div class="feature-card">
            <h4>🤖 AI-Generated</h4>
            <p>Documentation created by analyzing Flask code with Pydantic AI agents</p>
        </div>
        <div class="feature-card">
            <h4>🔧 Ready-to-Test</h4>
            <p>Use "Try it out" buttons to test endpoints directly from the browser</p>
        </div>
        <div class="feature-card">
            <h4>📋 Curl Examples</h4>
            <p>Each endpoint includes example curl commands for terminal testing</p>
        </div>
        <div class="feature-card">
            <h4>⚡ Real-time</h4>
            <p>Hosted locally with live reloading for development</p>
        </div>
    </div>
    
    <div class="info-bar">
        <h3>🧪 How to Test Your API</h3>
        <ol>
            <li><strong>Interactive Testing:</strong> Use the "Try it out" button in each endpoint below</li>
            <li><strong>Curl Commands:</strong> Copy curl examples from endpoint descriptions</li>
            <li><strong>External Tools:</strong> Use the OpenAPI spec URL with Postman, Insomnia, etc.</li>
        </ol>
        <p><strong>💡 Pro Tip:</strong> Make sure your Flask API is running on <code>http://localhost:5000</code> before testing!</p>
    </div>
    
    <div id="swagger-ui"></div>
    
    <script src="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui-bundle.js"></script>
    <script src="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui-standalone-preset.js"></script>
    <script>
    window.onload = function() {
        const ui = SwaggerUIBundle({
            url: '/api/openapi.json',
            dom_id: '#swagger-ui',
            deepLinking: true,
            presets: [
                SwaggerUIBundle.presets.apis,
                SwaggerUIStandalonePreset
            ],
            plugins: [
                SwaggerUIBundle.plugins.DownloadUrl
            ],
            layout: "StandaloneLayout",
            tryItOutEnabled: true,
            supportedSubmitMethods: ['get', 'post', 'put', 'delete', 'patch'],
            onComplete: function() {
                console.log('🎉 Swagger UI loaded successfully!');
                console.log('📋 OpenAPI spec loaded from: /api/openapi.json');
            },
            onFailure: function(error) {
                console.error('❌ Failed to load Swagger UI:', error);
            }
        });
        
        window.ui = ui;
    };
    </script>
</body>
</html>
"""

@app.route('/')
def swagger_ui():
    """Serve the Swagger UI interface"""
    host_url = f"http://localhost:{app.config.get('PORT', 8080)}"
    return render_template_string(SWAGGER_UI_HTML, host_url=host_url)

@app.route('/api/openapi.json')
def openapi_spec():
    """Serve the OpenAPI specification JSON"""
    try:
        # Read the generated OpenAPI spec
        spec_path = os.path.join(os.path.dirname(__file__), 'docs', 'openapi_pydantic_ai.json')
        
        if not os.path.exists(spec_path):
            return jsonify({
                "error": "OpenAPI specification not found",
                "message": "Please run generate_docs_pydantic_ai.py first to generate the OpenAPI spec",
                "expected_path": spec_path
            }), 404
        
        with open(spec_path, 'r') as f:
            spec_data = json.load(f)
        
        return jsonify(spec_data)
    
    except Exception as e:
        return jsonify({
            "error": "Failed to load OpenAPI specification",
            "message": str(e)
        }), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "Swagger UI Server",
        "openapi_spec": "/api/openapi.json",
        "documentation": "/"
    })

def open_browser(url):
    """Open browser after a delay to ensure server is running"""
    time.sleep(1.5)  # Wait for server to start
    try:
        webbrowser.open(url)
        print(f"✅ Opened browser at: {url}")
    except Exception as e:
        print(f"⚠️  Could not open browser automatically: {e}")
        print(f"🔗 Please manually open: {url}")

def main():
    """Main function to run the Swagger UI server"""
    
    # Check if OpenAPI spec exists
    spec_path = os.path.join(os.path.dirname(__file__), 'docs', 'openapi_pydantic_ai.json')
    
    if not os.path.exists(spec_path):
        print("❌ OpenAPI specification not found!")
        print(f"📁 Expected location: {spec_path}")
        print("🔧 Please run 'python generate_docs_pydantic_ai.py' first to generate the OpenAPI spec")
        return
    
    # Configuration
    HOST = '0.0.0.0'  # Allow external access
    PORT = 8080
    
    app.config['PORT'] = PORT
    
    # Server info
    local_url = f"http://localhost:{PORT}"
    
    print("🚀 Starting Swagger UI Server...")
    print("=" * 60)
    print(f"📊 OpenAPI Spec: {spec_path}")
    print(f"🌐 Swagger UI URL: {local_url}")
    print(f"📋 OpenAPI JSON URL: {local_url}/api/openapi.json")
    print(f"🔍 Health Check: {local_url}/health")
    print("=" * 60)
    print("📱 Server Features:")
    print("  • Interactive API documentation")
    print("  • Real-time endpoint testing")
    print("  • Curl command examples")
    print("  • OpenAPI 3.0 compliant")
    print("  • Responsive design")
    print("=" * 60)
    print("🔧 Usage Instructions:")
    print("1. 📖 View documentation in your browser")
    print("2. 🧪 Test endpoints using 'Try it out' buttons")
    print("3. 📋 Copy curl commands for terminal testing")
    print("4. 🔗 Share the URL with your team")
    print("=" * 60)
    print("⏹️  Press Ctrl+C to stop the server")
    print()
    
    # Open browser in a separate thread
    browser_thread = threading.Thread(target=open_browser, args=(local_url,))
    browser_thread.daemon = True
    browser_thread.start()
    
    try:
        # Run the Flask server
        app.run(
            host=HOST,
            port=PORT,
            debug=False,  # Set to True for development
            use_reloader=False  # Disable to prevent double startup
        )
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Server error: {e}")
    finally:
        print("👋 Goodbye!")

if __name__ == "__main__":
    main()
