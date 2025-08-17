# 🤖 Auto-DocGen: AI-Powered API Documentation Generator

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenAPI 3.0](https://img.shields.io/badge/OpenAPI-3.0-green.svg)](https://swagger.io/specification/)

**Auto-DocGen** is an intelligent documentation generator that uses **Pydantic AI agents** with **GPT-3.5-turbo** to automatically analyze your Flask applications and generate comprehensive **OpenAPI 3.0** documentation with interactive **Swagger UI**.

![Demo](https://img.shields.io/badge/Demo-Live-brightgreen) *(Replace with actual demo GIF/screenshot)*

## ✨ Features

- 🤖 **AI-Powered Analysis**: Uses Pydantic AI agents with GPT-3.5-turbo to understand your Flask code
- 📋 **OpenAPI 3.0 Compliant**: Generates industry-standard API documentation
- 🌐 **Interactive Swagger UI**: Beautiful, responsive web interface for testing APIs
- 🔧 **Ready-to-Use Curl Commands**: Each endpoint includes working curl examples
- ⚡ **Real-time Testing**: Test endpoints directly from the browser
- 🎯 **Minimal Setup**: Just point it at your Flask app and go
- 🔄 **Flexible Architecture**: Easy to extend and customize

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Flask application to document

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/auto-docgen.git
   cd auto-docgen
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   # Create .env file
   echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
   ```

### Usage

#### Step 1: Generate Documentation

```bash
# Generate OpenAPI documentation from your Flask app
python generate_docs_pydantic_ai.py
```

This will:
- Analyze your Flask endpoints using AI
- Generate `docs/openapi_pydantic_ai.json`
- Create a Swagger UI HTML file

#### Step 2: Serve Documentation

```bash
# Start the Swagger UI server
python serve_swagger_ui.py
```

Your documentation will be available at:
- **Swagger UI**: http://localhost:8080
- **OpenAPI JSON**: http://localhost:8080/api/openapi.json
- **Health Check**: http://localhost:8080/health

## 📁 Project Structure

```
auto-docgen/
├── 📄 README.md                    # This file
├── 📋 requirements.txt             # Python dependencies
├── 🔧 generate_docs_pydantic_ai.py # Main documentation generator
├── 🌐 serve_swagger_ui.py          # Swagger UI server
├── 📝 parser.py                    # Flask app parser
├── 🎯 app.py                       # Example Flask application
├── 📚 docs/                        # Generated documentation
│   ├── openapi_pydantic_ai.json   # OpenAPI specification
│   └── index_pydantic_ai.html     # Static Swagger UI
└── 🧪 examples/                    # Example applications
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional
FLASK_APP_PATH=app.py              # Path to your Flask app
API_BASE_URL=http://localhost:5000 # Base URL for your API
```

### Customizing the Parser

Edit `parser.py` to point to your Flask application:

```python
# Update this to point to your Flask app
from your_app import app

# The parser will automatically discover all routes
endpoints = get_endpoints(app)
```

## 🎯 Examples

### Basic Usage

```python
# Your Flask app (app.py)
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message='hello world')

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify(echo=data)

if __name__ == '__main__':
    app.run(debug=True)
```

Run the documentation generator:

```bash
python generate_docs_pydantic_ai.py
```

Generated documentation will include:
- Intelligent endpoint descriptions
- Request/response examples
- HTTP status codes
- Curl command examples

### Advanced Configuration

```python
# Custom configuration in generate_docs_pydantic_ai.py
agent = Agent(
    model='openai:gpt-3.5-turbo-0125',
    system_prompt="""
    Your custom prompt here for specialized documentation...
    """
)
```

## 🔍 API Reference

### Core Components

#### `generate_docs_pydantic_ai.py`
Main documentation generator using Pydantic AI agents.

**Key Functions:**
- `setup_pydantic_ai_agent()` - Initialize AI agent
- `pydantic_ai_query()` - Query AI for documentation
- `generate_fallback_response()` - Fallback when AI fails

#### `serve_swagger_ui.py`
Production-ready server for hosting Swagger UI.

**Endpoints:**
- `GET /` - Swagger UI interface
- `GET /api/openapi.json` - OpenAPI specification
- `GET /health` - Health check

#### `parser.py`
Flask application parser and endpoint discovery.

**Functions:**
- `get_endpoints()` - Extract routes from Flask app
- `get_function_code()` - Get source code of route functions

## 🛠️ Development

### Running Tests

```bash
# Run example tests
cd pratham-test
python test_generate_open_api.py
```

### Adding New Features

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

### Extending the AI Prompts

Customize the AI analysis by modifying the system prompt in `generate_docs_pydantic_ai.py`:

```python
system_prompt = """
Your custom AI instructions here...
- Analyze Flask endpoints
- Generate accurate documentation
- Include specific formatting
"""
```

## 📊 Comparison with Alternatives

| Feature | Auto-DocGen | Manual Docs | Other Tools |
|---------|-------------|-------------|-------------|
| AI-Powered | ✅ | ❌ | ❌ |
| Zero Config | ✅ | ❌ | ⚠️ |
| Curl Examples | ✅ | ❌ | ⚠️ |
| Real-time UI | ✅ | ❌ | ✅ |
| OpenAPI 3.0 | ✅ | ⚠️ | ✅ |
| Maintenance | ✅ Low | ❌ High | ⚠️ Medium |

## 🚨 Troubleshooting

### Common Issues

**Q: "OPENAI_API_KEY not found" error**
```bash
# Solution: Create .env file with your API key
echo "OPENAI_API_KEY=sk-your-key-here" > .env
```

**Q: "No endpoints found" error**
```bash
# Solution: Check your Flask app path in parser.py
# Make sure your Flask app is importable
```

**Q: Server won't start on port 8080**
```bash
# Solution: Kill existing process or use different port
lsof -ti:8080 | xargs kill -9
```

**Q: AI analysis fails**
```bash
# The system includes intelligent fallbacks
# Check your OpenAI API key and quota
```

### Debug Mode

Enable debug mode for troubleshooting:

```python
# In serve_swagger_ui.py
app.run(debug=True, port=8080)
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Clone and setup development environment
git clone https://github.com/your-username/auto-docgen.git
cd auto-docgen
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies
```

### Submitting Issues

- 🐛 **Bug reports**: Use the bug report template
- 💡 **Feature requests**: Use the feature request template
- 📖 **Documentation**: Help improve our docs

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Pydantic AI** - For the excellent AI agent framework
- **OpenAPI Initiative** - For the OpenAPI specification
- **Swagger UI** - For the beautiful documentation interface
- **Flask Community** - For the amazing web framework

## 📞 Support

- 📧 **Email**: support@auto-docgen.com
- 💬 **Discord**: [Join our community](https://discord.gg/auto-docgen)
- 🐛 **Issues**: [GitHub Issues](https://github.com/your-username/auto-docgen/issues)
- 📖 **Docs**: [Full Documentation](https://auto-docgen.readthedocs.io)

## 🔮 Roadmap

- [ ] Support for FastAPI applications
- [ ] Custom AI model integration
- [ ] Docker containerization
- [ ] CI/CD pipeline templates
- [ ] Multi-language support
- [ ] Plugin architecture
- [ ] Cloud deployment options

---

**Made with ❤️ by the Auto-DocGen Team**

*Star ⭐ this repo if you find it useful!*
