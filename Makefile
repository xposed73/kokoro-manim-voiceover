.PHONY: help install install-dev test lint format clean build publish

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install the package
	pip install -e .

install-dev: ## Install development dependencies
	pip install -r requirements-dev.txt
	pre-commit install

test: ## Run tests
	pytest tests/ -v --cov=kokoro_mv --cov-report=html --cov-report=term

lint: ## Run linting
	flake8 .
	black --check .
	isort --check-only .
	mypy .

format: ## Format code
	black .
	isort .

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build: ## Build the package
	python -m build

publish: ## Publish to PyPI (requires PYPI_API_TOKEN)
	twine upload dist/*

check-imports: ## Test that imports work
	python -c "from kokoro_mv import KokoroService, __version__; print(f'✅ Import successful! Version: {__version__}')"

setup-test: ## Test the setup module
	python -c "from kokoro_mv.setup import main; print('✅ Setup module imported successfully!')"
