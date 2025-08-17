# 🤝 Contributing to Auto-DocGen

Thank you for your interest in contributing to Auto-DocGen! This document provides guidelines and information for contributors.

## 🚀 Quick Start

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/auto-docgen.git
   cd auto-docgen
   ```
3. **Set up development environment**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```
4. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

## 🛠️ Development Guidelines

### Code Style

- Follow **PEP 8** Python style guidelines
- Use **type hints** where appropriate
- Add **docstrings** to all functions and classes
- Keep functions **small and focused**
- Use **meaningful variable names**

### Example:
```python
def generate_openapi_docs(app: Flask, model: str = "gpt-3.5-turbo") -> Dict[str, Any]:
    """Generate OpenAPI documentation for a Flask application.
    
    Args:
        app: Flask application instance
        model: AI model to use for generation
        
    Returns:
        Dictionary containing OpenAPI specification
        
    Raises:
        ValueError: If app is not a valid Flask instance
    """
    # Implementation here
```

### Testing

- Write **unit tests** for new features
- Ensure **existing tests pass**
- Add **integration tests** for API endpoints
- Test with **different Flask app configurations**

```bash
# Run tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_generator.py::test_basic_endpoint
```

### Documentation

- Update **README.md** for new features
- Add **examples** for complex functionality
- Include **docstrings** in code
- Update **API documentation**

## 📋 Types of Contributions

### 🐛 Bug Reports

When reporting bugs, please include:

- **Python version** and operating system
- **Auto-DocGen version**
- **Complete error message** and stack trace
- **Minimal code example** that reproduces the issue
- **Expected vs actual behavior**

**Template:**
```markdown
## Bug Description
Brief description of the issue

## Environment
- Python: 3.9.0
- Auto-DocGen: 1.0.0
- OS: macOS 12.0

## Steps to Reproduce
1. Step one
2. Step two
3. Step three

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Code Example
```python
# Minimal example
```

### 💡 Feature Requests

For new features, please provide:

- **Clear description** of the feature
- **Use case** and motivation
- **Proposed implementation** (if you have ideas)
- **Examples** of how it would be used

### 🔧 Code Contributions

#### Areas We Need Help With:

1. **Framework Support**
   - FastAPI integration
   - Django REST framework support
   - Quart async support

2. **AI Model Integration**
   - Additional AI providers (Anthropic, Cohere)
   - Custom model fine-tuning
   - Prompt optimization

3. **Documentation Features**
   - Response schema inference
   - Authentication documentation
   - Rate limiting documentation

4. **UI/UX Improvements**
   - Enhanced Swagger UI themes
   - Custom CSS templates
   - Mobile-responsive design

5. **DevOps & Infrastructure**
   - Docker containerization
   - CI/CD pipeline improvements
   - Performance optimizations

#### Pull Request Process:

1. **Create an issue** first (unless it's a small fix)
2. **Fork and create a branch** from `main`
3. **Make your changes** with clear commit messages
4. **Add tests** for new functionality
5. **Update documentation** as needed
6. **Ensure all tests pass**
7. **Submit a pull request**

#### Commit Message Guidelines:

```bash
# Format: type(scope): description

feat(ai): add support for GPT-4 model
fix(parser): handle edge case in route discovery
docs(readme): update installation instructions
test(generator): add tests for error handling
refactor(ui): improve swagger template structure
```

#### Pull Request Template:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] Added unit tests
- [ ] Added integration tests
- [ ] Manual testing completed
- [ ] All existing tests pass

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
```

## 🏗️ Development Setup

### Prerequisites

- Python 3.8+
- OpenAI API key
- Git

### Setup Steps

```bash
# Clone the repository
git clone https://github.com/your-username/auto-docgen.git
cd auto-docgen

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8 mypy

# Set up environment variables
cp .env.example .env
# Edit .env with your OpenAI API key

# Run tests to ensure everything works
python -m pytest
```

### Development Workflow

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes
# ... edit files ...

# Run tests
python -m pytest

# Format code
black .

# Check style
flake8 .

# Type checking
mypy .

# Commit changes
git add .
git commit -m "feat: add your feature description"

# Push and create PR
git push origin feature/your-feature-name
```

## 📝 Code Review Guidelines

### For Reviewers:

- **Be constructive** and helpful
- **Explain the "why"** behind suggestions
- **Test the changes** locally when possible
- **Check for breaking changes**
- **Verify documentation** is updated

### For Contributors:

- **Respond promptly** to review feedback
- **Ask questions** if feedback is unclear
- **Test your changes** thoroughly
- **Keep discussions** focused on the code

## 🌟 Recognition

Contributors are recognized in:

- **README.md** contributors section
- **Release notes** for significant contributions
- **GitHub contributors** page
- **Special mentions** in project updates

## 📞 Getting Help

- **Discord**: [Join our community](https://discord.gg/auto-docgen)
- **GitHub Discussions**: For general questions
- **GitHub Issues**: For bug reports and feature requests
- **Email**: maintainers@auto-docgen.com

## 📄 License

By contributing, you agree that your contributions will be licensed under the same [MIT License](LICENSE) that covers the project.

---

**Thank you for contributing to Auto-DocGen! 🎉**
