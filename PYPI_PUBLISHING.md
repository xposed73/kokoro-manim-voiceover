# PyPI Publishing Guide

This document provides step-by-step instructions for publishing the `kokoro-manim-voiceover` package to PyPI.

## Prerequisites

1. **PyPI Account**: Create an account at [pypi.org](https://pypi.org) if you don't have one
2. **TestPyPI Account**: Create an account at [test.pypi.org](https://test.pypi.org) for testing
3. **API Tokens**: Generate API tokens for both PyPI and TestPyPI

## Setup API Tokens

### For PyPI (Production)
1. Go to [pypi.org/manage/account/](https://pypi.org/manage/account/)
2. Create a new API token with scope "Entire account" or "Specific project"
3. Save the token securely

### For TestPyPI (Testing)
1. Go to [test.pypi.org/manage/account/](https://test.pypi.org/manage/account/)
2. Create a new API token
3. Save the token securely

## Configure Credentials

Create a `.pypirc` file in your home directory:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-your-api-token-here

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-your-testpypi-token-here
```

## Publishing Workflow

### Option 1: Using the Helper Script

```bash
# Build and check the package
python publish.py all

# Test on TestPyPI first
python publish.py test

# If test is successful, publish to PyPI
python publish.py publish
```

### Option 2: Manual Commands

```bash
# 1. Clean previous builds
python publish.py clean

# 2. Build the package
python -m build

# 3. Check the package
twine check dist/*

# 4. Test on TestPyPI
twine upload --repository testpypi dist/*

# 5. Install from TestPyPI to verify
pip install --index-url https://test.pypi.org/simple/ kokoro-manim-voiceover

# 6. If everything works, publish to PyPI
twine upload dist/*
```

## Automated Publishing with GitHub Actions

The repository includes a GitHub Actions workflow (`.github/workflows/publish.yml`) that automatically publishes to PyPI when you create a release.

### To use automated publishing:

1. **Enable Trusted Publishing** (Recommended):
   - Go to your PyPI project settings
   - Add your GitHub repository as a trusted publisher
   - Configure the workflow to use trusted publishing

2. **Create a Release**:
   ```bash
   git tag v0.1.3
   git push origin v0.1.3
   ```
   Then create a release on GitHub with the same tag.

3. **Manual Trigger**:
   - Go to Actions tab in GitHub
   - Run the "Publish to PyPI" workflow manually

## Version Management

### Updating Version

1. Update version in `pyproject.toml`:
   ```toml
   version = "0.1.4"
   ```

2. Update version in `kokoro_mv/__init__.py`:
   ```python
   __version__ = "0.1.4"
   ```

3. Update `CHANGELOG.md` with new changes

4. Commit and tag:
   ```bash
   git add .
   git commit -m "Bump version to 0.1.4"
   git tag v0.1.4
   git push origin main --tags
   ```

## Package Structure

The package is structured as follows:

```
kokoro-manim-voiceover/
├── kokoro_mv/              # Main package
│   ├── __init__.py        # Package initialization
│   ├── koko.py            # Main KokoroService class
│   └── setup.py           # Setup utilities
├── .github/
│   └── workflows/
│       └── publish.yml    # GitHub Actions workflow
├── pyproject.toml         # Package configuration
├── MANIFEST.in            # Files to include in distribution
├── README.md              # Package documentation
├── CHANGELOG.md           # Version history
├── LICENSE                # MIT license
└── publish.py             # Publishing helper script
```

## Verification

After publishing, verify the package:

1. **Check PyPI page**: Visit https://pypi.org/project/kokoro-manim-voiceover/
2. **Test installation**: `pip install kokoro-manim-voiceover`
3. **Test import**: `python -c "import kokoro_mv; print(kokoro_mv.__version__)"`

## Troubleshooting

### Common Issues

1. **Package already exists**: Increment version number
2. **Authentication failed**: Check API tokens in `.pypirc`
3. **Build fails**: Check `pyproject.toml` syntax
4. **Upload fails**: Ensure package name is unique

### Getting Help

- [PyPI Documentation](https://packaging.python.org/tutorials/packaging-projects/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Setuptools Documentation](https://setuptools.pypa.io/)

## Security Notes

- Never commit API tokens to version control
- Use environment variables for CI/CD
- Enable 2FA on PyPI accounts
- Use trusted publishing when possible
