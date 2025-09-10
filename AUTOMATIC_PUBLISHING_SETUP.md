# Automatic PyPI Publishing Setup

This guide will help you set up automatic publishing to PyPI whenever you create a GitHub release.

## Prerequisites

1. **GitHub Repository**: Your code should be in a GitHub repository
2. **PyPI Account**: Create an account at [pypi.org](https://pypi.org) if you don't have one
3. **Package Name**: Ensure your package name is available on PyPI

## Step 1: Set Up PyPI Trusted Publishing (Recommended)

Trusted publishing is the most secure way to publish to PyPI automatically.

### 1.1 Create PyPI Project (if not exists)
1. Go to [pypi.org](https://pypi.org)
2. Log in to your account
3. Go to "Your projects" → "Add a new project"
4. Enter project name: `kokoro-manim-voiceover`
5. Leave it empty for now (we'll upload via GitHub Actions)

### 1.2 Configure Trusted Publishing
1. Go to your project on PyPI: https://pypi.org/project/kokoro-manim-voiceover/
2. Click "Manage" → "Publishing" → "Add a new pending publisher"
3. Fill in the details:
   - **PyPI project name**: `kokoro-manim-voiceover`
   - **Owner**: `nkayzai` (your GitHub username)
   - **Repository name**: `kokoro-manim-voiceover`
   - **Workflow filename**: `publish.yml`
   - **Environment name**: (leave empty)
4. Click "Add"

## Step 2: Push Your Code to GitHub

```bash
# Initialize git if not already done
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit: Ready for PyPI publishing"

# Add your GitHub repository as remote
git remote add origin https://github.com/nkayzai/kokoro-manim-voiceover.git

# Push to GitHub
git push -u origin main
```

## Step 3: Create Your First Release

### Option A: Using GitHub Web Interface
1. Go to your repository on GitHub
2. Click "Releases" → "Create a new release"
3. Choose a tag version: `v0.1.3`
4. Release title: `v0.1.3`
5. Description: Copy from your CHANGELOG.md
6. Click "Publish release"

### Option B: Using Git Commands
```bash
# Create and push a tag
git tag v0.1.3
git push origin v0.1.3

# Then create release on GitHub web interface
```

## Step 4: Monitor the Publishing Process

1. Go to your repository → "Actions" tab
2. You should see a "Publish to PyPI" workflow running
3. Click on it to see the progress
4. The workflow will:
   - Build your package
   - Check it for issues
   - Publish to PyPI automatically

## Step 5: Verify Publication

1. Check your package on PyPI: https://pypi.org/project/kokoro-manim-voiceover/
2. Test installation: `pip install kokoro-manim-voiceover`
3. Verify it works: `python -c "import kokoro_mv; print(kokoro_mv.__version__)"`

## Future Releases

For future releases, simply:

1. **Update version** in `pyproject.toml` and `kokoro_mv/__init__.py`
2. **Update CHANGELOG.md** with new changes
3. **Commit and push**:
   ```bash
   git add .
   git commit -m "Bump version to 0.1.4"
   git push
   ```
4. **Create a new release** on GitHub with the new version tag
5. **PyPI publishing happens automatically!**

## Troubleshooting

### Common Issues

1. **Workflow fails with "403 Forbidden"**:
   - Check that trusted publishing is properly configured
   - Ensure the repository name and workflow filename match exactly

2. **Package name already exists**:
   - Change the package name in `pyproject.toml`
   - Update trusted publishing configuration

3. **Workflow doesn't trigger**:
   - Make sure you created a "release" (not just a tag)
   - Check that the workflow file is in `.github/workflows/`

### Manual Workflow Trigger

You can also trigger the workflow manually:
1. Go to "Actions" tab in your repository
2. Click "Publish to PyPI"
3. Click "Run workflow"

## Security Benefits of Trusted Publishing

- ✅ No API tokens to manage
- ✅ No secrets to store in GitHub
- ✅ PyPI verifies the request comes from your repository
- ✅ More secure than API token-based publishing

## Alternative: API Token Method

If you prefer using API tokens instead of trusted publishing:

1. Create a PyPI API token
2. Add it as a GitHub secret named `PYPI_API_TOKEN`
3. Update the workflow to use the token

But trusted publishing is recommended for better security.

## Next Steps

Once everything is set up:
1. Your package will automatically publish to PyPI on every release
2. Users can install it with `pip install kokoro-manim-voiceover`
3. You can focus on development while publishing happens automatically!

## Support

If you encounter issues:
- Check the GitHub Actions logs
- Verify PyPI trusted publishing configuration
- Ensure your package name is unique on PyPI
