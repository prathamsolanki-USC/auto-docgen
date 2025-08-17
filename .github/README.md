# 🤖 GitHub Actions Workflows for Auto-DocGen

This directory contains CI/CD workflows that automatically maintain and update your API documentation.

## 🔄 Available Workflows

### 1. Auto-Update API Documentation (`auto-docs-update.yml`)

**Triggers:**
- ✅ Push to `main` or `develop` branches (Python files)
- ✅ Pull requests to `main` (Python files)
- ✅ Manual trigger via GitHub Actions UI

**What it does:**
- 🔍 **Detects API changes** in Python files, Flask apps, examples
- 🤖 **Generates documentation** using Pydantic AI + GPT-3.5-turbo
- 📊 **Provides statistics** about generated endpoints
- 📤 **Auto-commits** updated documentation
- 🌐 **Deploys to GitHub Pages** for public access

**Features:**
- Smart change detection (only runs when needed)
- Detailed commit messages with generation stats
- Enhanced Swagger UI with timestamps
- Automatic GitHub Pages deployment
- Comprehensive error handling and fallbacks

### 2. Test & Validate (`test-and-validate.yml`)

**Triggers:**
- ✅ Push to `main` or `develop` branches
- ✅ Pull requests to `main`
- ✅ Manual trigger

**What it does:**
- 🔍 **Code quality checks** (flake8, black, isort, mypy)
- 🧪 **Tests documentation generation** functionality
- 📚 **Validates example applications**
- 🔒 **Security scanning** with Bandit
- 🐍 **Multi-Python version testing** (3.8, 3.9, 3.10, 3.11)

### 3. Manual Documentation Update (`manual-docs-update.yml`)

**Triggers:**
- ✅ Manual trigger only (GitHub Actions UI)

**What it does:**
- 🎛️ **Customizable AI model** selection (GPT-3.5, GPT-4, GPT-4-turbo)
- 🎯 **Specify target Flask app** to document
- 🔄 **Force update option** even without changes
- 📊 **Compare with previous** documentation
- 🧹 **Automatic cleanup** and security

**Use Cases:**
- Testing different AI models
- Documenting specific Flask applications
- Force refresh after configuration changes
- Manual quality checks

## 🔧 Setup Requirements

### 1. GitHub Repository Settings

#### Enable GitHub Pages:
1. Go to **Settings** → **Pages**
2. Source: **GitHub Actions**
3. Your docs will be available at: `https://your-username.github.io/auto-docgen/`

#### Required Secrets:
Add to **Settings** → **Secrets and variables** → **Actions**:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

#### Permissions:
Ensure **Settings** → **Actions** → **General**:
- ✅ **Read and write permissions**
- ✅ **Allow GitHub Actions to create and approve pull requests**

### 2. Repository Structure

Ensure your repository has:
```
auto-docgen/
├── .github/workflows/          # CI/CD workflows
├── docs/                       # Generated documentation
├── examples/                   # Example Flask apps
├── generate_docs_pydantic_ai.py
├── parser.py
├── app.py
└── requirements.txt
```

## 🚀 Usage Examples

### Automatic Updates

**Scenario 1:** You modify a Flask endpoint
```python
# In app.py - add new endpoint
@app.route('/new-endpoint', methods=['POST'])
def new_endpoint():
    return jsonify({"message": "New feature!"})
```

**Result:**
1. 🔍 Push triggers change detection
2. 🤖 AI analyzes new endpoint
3. 📚 Documentation auto-updates
4. 🌐 GitHub Pages refreshes
5. 📧 You get notified of completion

### Manual Updates

**Scenario 2:** You want to test GPT-4 for documentation
1. Go to **Actions** → **Manual Documentation Update**
2. Click **Run workflow**
3. Select **GPT-4** model
4. Specify target app: `examples/basic_api.py`
5. Check **Force update**
6. Click **Run workflow**

**Result:**
- 🧠 Uses GPT-4 instead of GPT-3.5
- 📊 Compares with previous docs
- 📝 Creates detailed commit with model info
- 🎨 Enhanced UI shows manual update badge

## 📊 Workflow Outputs

### Documentation URL
After successful runs, your documentation is available at:
```
https://your-username.github.io/auto-docgen/
```

### Commit Messages
Auto-generated commits include:
- 📊 Number of endpoints processed
- 🔄 What triggered the update
- 📝 List of changed files
- 🕐 Generation timestamp
- 🤖 AI model used

### GitHub Pages
Your documentation site includes:
- 🌐 Interactive Swagger UI
- 📋 Raw OpenAPI JSON specification
- 🕐 Last updated timestamp
- 🤖 Generation method info

## 🔍 Monitoring & Debugging

### Check Workflow Status
- Go to **Actions** tab in your repository
- View individual workflow runs
- Check logs for detailed output

### Common Issues

**Issue:** `OPENAI_API_KEY not found`
```bash
# Solution: Add to repository secrets
Settings → Secrets → Actions → New repository secret
Name: OPENAI_API_KEY
Value: your_actual_api_key
```

**Issue:** GitHub Pages not updating
```bash
# Solution: Check Pages settings
Settings → Pages → Source: GitHub Actions
```

**Issue:** No changes detected
```bash
# Solution: Trigger manual update
Actions → Manual Documentation Update → Run workflow
Check "Force update" option
```

## 🎯 Best Practices

### 1. Branch Protection
Set up branch protection rules:
- ✅ Require status checks (Test & Validate)
- ✅ Require up-to-date branches
- ✅ Include administrators

### 2. Monitoring
- 📧 Enable email notifications for failed workflows
- 👀 Review auto-generated documentation periodically
- 📊 Monitor GitHub Pages deployment status

### 3. Security
- 🔒 Keep `OPENAI_API_KEY` in secrets only
- 🔍 Regularly review workflow permissions
- 🧹 Cleanup is automatic (temp files removed)

## 🤝 Contributing

To modify workflows:
1. Fork the repository
2. Edit workflow files in `.github/workflows/`
3. Test changes in your fork first
4. Submit pull request

---

**🎉 Your Auto-DocGen CI/CD is now ready to automatically maintain your API documentation!**
