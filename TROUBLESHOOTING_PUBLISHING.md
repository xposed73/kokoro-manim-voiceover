# Troubleshooting PyPI Publishing Issues

## Current Issue: Workflow Failures

Your GitHub Actions workflow is failing because the PyPI trusted publishing is not set up yet. Here's how to fix it:

## Step 1: Set Up PyPI Trusted Publishing

### 1.1 Create PyPI Project
1. Go to [pypi.org](https://pypi.org) and log in
2. Click "Your projects" → "Add a new project"
3. Enter project name: `kokoro-manim-voiceover`
4. **Leave the project empty** (don't upload anything yet)
5. Click "Create project"

### 1.2 Configure Trusted Publishing
1. Go to your project: https://pypi.org/project/kokoro-manim-voiceover/
2. Click "Manage" → "Publishing" → "Add a new pending publisher"
3. Fill in the details:
   - **PyPI project name**: `kokoro-manim-voiceover`
   - **Owner**: `nkayzai` (your GitHub username)
   - **Repository name**: `kokoro-manim-voiceover`
   - **Workflow filename**: `publish.yml`
   - **Environment name**: `pypi`
4. Click "Add"

## Step 2: Create GitHub Environment

### 2.1 Set Up Environment in GitHub
1. Go to your repository: https://github.com/nkayzai/kokoro-manim-voiceover
2. Click "Settings" → "Environments"
3. Click "New environment"
4. Name it: `pypi`
5. Click "Configure environment"
6. **Optional**: Add protection rules (like requiring manual approval)
7. Click "Save protection rules"

## Step 3: Test the Workflow

### 3.1 Create a Test Release
1. Go to your repository → "Releases"
2. Click "Create a new release"
3. Choose tag: `v0.1.3` (already exists)
4. Release title: `v0.1.3`
5. Description: Copy from `CHANGELOG.md`
6. Click "Publish release"

### 3.2 Monitor the Workflow
1. Go to "Actions" tab
2. You should see "Publish to PyPI" workflow running
3. Check the logs if it fails

## Common Issues and Solutions

### Issue 1: "403 Forbidden" Error
**Cause**: Trusted publishing not configured properly
**Solution**: 
- Double-check the PyPI trusted publishing settings
- Ensure repository name and workflow filename match exactly
- Make sure the GitHub environment is named `pypi`

### Issue 2: "Package not found" Error
**Cause**: PyPI project doesn't exist
**Solution**: Create the project on PyPI first (Step 1.1)

### Issue 3: Workflow doesn't trigger
**Cause**: No release created
**Solution**: Create a GitHub release (Step 3.1)

### Issue 4: "Environment not found" Error
**Cause**: GitHub environment not created
**Solution**: Create the `pypi` environment (Step 2.1)

## Alternative: Manual Publishing (If Trusted Publishing Fails)

If you continue having issues with trusted publishing, you can use API tokens:

### 1. Create PyPI API Token
1. Go to [pypi.org/manage/account/](https://pypi.org/manage/account/)
2. Create a new API token
3. Copy the token

### 2. Add GitHub Secret
1. Go to your repository → "Settings" → "Secrets and variables" → "Actions"
2. Click "New repository secret"
3. Name: `PYPI_API_TOKEN`
4. Value: Your PyPI API token
5. Click "Add secret"

### 3. Update Workflow
Replace the publish step in `.github/workflows/publish.yml` with:
```yaml
- name: Publish to PyPI
  uses: pypa/gh-action-pypi-publish@release/v1
  with:
    password: ${{ secrets.PYPI_API_TOKEN }}
```

## Testing Your Setup

### Test 1: Check Package Builds
```bash
# In your local repository
python -m build
twine check dist/*
```

### Test 2: Test Upload to TestPyPI
```bash
# Upload to TestPyPI first
twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ kokoro-manim-voiceover
```

### Test 3: Verify on PyPI
1. Check your package: https://pypi.org/project/kokoro-manim-voiceover/
2. Test installation: `pip install kokoro-manim-voiceover`
3. Test import: `python -c "import kokoro_mv; print(kokoro_mv.__version__)"`

## Next Steps After Fixing

Once the workflow is working:

1. **For future releases**:
   - Update version in `pyproject.toml` and `kokoro_mv/__init__.py`
   - Update `CHANGELOG.md`
   - Commit and push
   - Create a new tag: `git tag v0.1.4 && git push origin v0.1.4`
   - Create GitHub release with the new tag

2. **Monitor the workflow**:
   - Check Actions tab after each release
   - Verify package appears on PyPI

## Getting Help

If you're still having issues:
1. Check the GitHub Actions logs for specific error messages
2. Verify all settings match exactly (case-sensitive)
3. Try the manual API token method as a fallback
4. Check PyPI's trusted publishing documentation

## Success Indicators

You'll know it's working when:
- ✅ GitHub Actions workflow completes successfully
- ✅ Package appears on PyPI
- ✅ You can install with `pip install kokoro-manim-voiceover`
- ✅ No more workflow failures in the Actions tab
