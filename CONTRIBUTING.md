# Contributing to Kokoro Manim Voiceover

Thank you for your interest in contributing to Kokoro Manim Voiceover! This document provides guidelines and information for contributors.

## Getting Started

### Prerequisites
- Python 3.11 or higher
- Git
- Basic knowledge of Python and Manim

### Setting up the Development Environment

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/your-username/kokoro-manim-voiceover.git
   cd kokoro-manim-voiceover
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Install pre-commit hooks**
   ```bash
   pre-commit install
   ```

5. **Install the package in development mode**
   ```bash
   pip install -e .
   ```

## Development Workflow

### Code Style
We use several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **pytest**: Testing

Run these tools before committing:
```bash
black .
isort .
flake8 .
mypy .
pytest
```

### Pre-commit Hooks
Pre-commit hooks will automatically run these tools when you commit. Make sure to install them:
```bash
pre-commit install
```

### Testing
- Write tests for new features
- Ensure all tests pass: `pytest`
- Aim for good test coverage

### Documentation
- Update docstrings for new functions/classes
- Update README.md if needed
- Add examples for new features

## Submitting Changes

### Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write code following the style guidelines
   - Add tests for new functionality
   - Update documentation as needed

3. **Test your changes**
   ```bash
   pytest
   python -c "from kokoro_mv import KokoroService; print('Import successful!')"
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: brief description of changes"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Use the provided PR template
   - Provide a clear description of changes
   - Link any related issues

### Commit Message Format
Use clear, descriptive commit messages:
- `Add: new feature description`
- `Fix: bug description`
- `Update: change description`
- `Remove: removal description`
- `Docs: documentation update`

## Issue Reporting

### Bug Reports
When reporting bugs, please include:
- Python version
- OS information
- Kokoro Manim Voiceover version
- Steps to reproduce
- Expected vs actual behavior
- Error messages (if any)

### Feature Requests
For feature requests, please include:
- Clear description of the feature
- Use case and motivation
- Potential implementation ideas (if any)

## Code of Conduct

### Our Pledge
We are committed to providing a welcoming and inclusive environment for all contributors.

### Expected Behavior
- Be respectful and inclusive
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards other community members

### Unacceptable Behavior
- Harassment, trolling, or discrimination
- Personal attacks or political discussions
- Spam or off-topic discussions
- Any other unprofessional conduct

## Release Process

Releases are managed through GitHub Actions:
1. Update version in `pyproject.toml`
2. Create a git tag: `git tag v0.1.1`
3. Push the tag: `git push origin v0.1.1`
4. GitHub Actions will automatically build and publish to PyPI

## Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Email**: nadeemak755@gmail.com

## License

By contributing to Kokoro Manim Voiceover, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🎉
