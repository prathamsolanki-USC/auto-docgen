# 📚 Examples

This directory contains example Flask applications that demonstrate Auto-DocGen's capabilities.

## 🎯 Available Examples

### 1. Basic API (`basic_api.py`)

A comprehensive REST API example featuring:
- **User Management**: CRUD operations for users
- **Post Management**: Blog-style posts with filtering
- **Health Checks**: Monitoring endpoints
- **Error Handling**: Proper HTTP status codes
- **Query Parameters**: Filtering and pagination
- **Sample Data**: Pre-loaded for testing

**Features Demonstrated:**
- GET, POST, PUT, DELETE operations
- Path parameters (`/users/<user_id>`)
- Query parameters (`/posts?author=john&limit=10`)
- Request body validation
- Error responses with proper status codes
- JSON responses with nested data

**To Run:**
```bash
cd examples
python basic_api.py
```

**To Generate Documentation:**
```bash
# Update parser.py to import from examples.basic_api
# Then run:
python generate_docs_pydantic_ai.py
```

### 2. Advanced Examples (Coming Soon)

- **E-commerce API**: Product catalog, orders, payments
- **Social Media API**: Posts, comments, likes, follows
- **File Upload API**: Image uploads, file management
- **Authentication API**: JWT tokens, OAuth integration

## 🔧 Using Examples with Auto-DocGen

### Method 1: Direct Import

1. Update `parser.py` to import your example:
   ```python
   from examples.basic_api import app
   ```

2. Run the documentation generator:
   ```bash
   python generate_docs_pydantic_ai.py
   ```

### Method 2: Copy and Modify

1. Copy an example to your project
2. Modify it to match your needs
3. Update `parser.py` to point to your app
4. Generate documentation

## 📊 Example Output

When you run Auto-DocGen on `basic_api.py`, you'll get:

- **12 endpoints** documented
- **Realistic examples** for each endpoint
- **Curl commands** for testing
- **Proper OpenAPI 3.0** specification
- **Interactive Swagger UI**

## 🧪 Testing Examples

Each example includes sample data and can be tested immediately:

```bash
# Start the API
python examples/basic_api.py

# Test in another terminal
curl http://localhost:5000/
curl http://localhost:5000/users
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com"}'
```

## 💡 Tips for Your Own APIs

Use these examples as templates for documenting your own APIs:

1. **Clear Function Names**: Use descriptive function names
2. **Docstrings**: Add docstrings to your route functions
3. **Error Handling**: Include proper error responses
4. **Type Hints**: Use type hints where possible
5. **Sample Data**: Include realistic example data

---

**Need help?** Check the main [README.md](../README.md) for full documentation.
