# 🔧 GitHub Repository Setup Guide

Follow these steps to enable automatic documentation updates for your Auto-DocGen repository.

## 📋 Quick Setup Checklist

### ✅ Step 1: Add OpenAI API Key

1. Go to your repository: https://github.com/prathamsolanki-USC/auto-docgen
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add:
   - **Name**: `OPENAI_API_KEY`
   - **Value**: Your actual OpenAI API key (starts with `sk-`)
5. Click **Add secret**

### ✅ Step 2: Enable GitHub Pages

1. Go to **Settings** → **Pages**
2. Under **Source**, select: **GitHub Actions**
3. Click **Save**

Your documentation will be available at:
```
https://prathamsolanki-USC.github.io/auto-docgen/
```

### ✅ Step 3: Configure Workflow Permissions

1. Go to **Settings** → **Actions** → **General**
2. Under **Workflow permissions**, select:
   - ✅ **Read and write permissions**
   - ✅ **Allow GitHub Actions to create and approve pull requests**
3. Click **Save**

### ✅ Step 4: Test the Setup

#### Option A: Automatic Test (Recommended)
1. Make a small change to any Python file (e.g., add a comment to `app.py`)
2. Commit and push the change
3. Go to **Actions** tab to watch the workflow run
4. Check your GitHub Pages URL after completion

#### Option B: Manual Test
1. Go to **Actions** → **Manual Documentation Update**
2. Click **Run workflow**
3. Leave default settings and click **Run workflow**
4. Watch the workflow complete
5. Check your GitHub Pages URL

## 🚀 What Happens Next

### Automatic Updates
After setup, documentation will automatically update when you:
- ✅ Modify any Python files
- ✅ Add new Flask endpoints
- ✅ Change existing API functionality
- ✅ Update examples

### Manual Updates
You can manually trigger updates:
- 🎛️ Choose different AI models (GPT-3.5, GPT-4, GPT-4-turbo)
- 🎯 Target specific Flask applications
- 🔄 Force updates even without changes

## 📊 Expected Results

### First Run
After setup, your first workflow will:
1. ✅ Analyze your Flask endpoints
2. ✅ Generate OpenAPI 3.0 documentation
3. ✅ Create interactive Swagger UI
4. ✅ Deploy to GitHub Pages
5. ✅ Commit updated docs to repository

### Ongoing Updates
Every time you change your API:
1. 🔍 Workflows detect changes automatically
2. 🤖 AI regenerates documentation
3. 📊 Statistics are included in commits
4. 🌐 GitHub Pages updates automatically

## 🔗 Important URLs

After setup, bookmark these:

- **Repository**: https://github.com/prathamsolanki-USC/auto-docgen
- **Documentation**: https://prathamsolanki-USC.github.io/auto-docgen/
- **Actions**: https://github.com/prathamsolanki-USC/auto-docgen/actions
- **Settings**: https://github.com/prathamsolanki-USC/auto-docgen/settings

## 🆘 Troubleshooting

### Issue: "OPENAI_API_KEY not found"
**Solution**: Double-check secret name (case-sensitive: `OPENAI_API_KEY`)

### Issue: GitHub Pages not working
**Solution**: Ensure Pages source is set to "GitHub Actions"

### Issue: Workflows not running
**Solution**: Check workflow permissions in repository settings

### Issue: Documentation not updating
**Solution**: Trigger manual update with "Force update" option

## 🎯 Next Steps

1. ✅ Complete the setup above
2. ✅ Test with a small change
3. ✅ Share your documentation URL with your team
4. ✅ Set up branch protection rules (optional)
5. ✅ Configure notification preferences

---

**🎉 Your Auto-DocGen CI/CD is ready! Documentation will now stay in sync with your code automatically.**
