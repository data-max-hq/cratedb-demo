# cratedb-demo

A Python project using CrateDB.

## Prerequisites

- Python 3.8 or higher
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cratedb-demo.git
cd cratedb-demo
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Activate the virtual environment:
```bash
poetry shell
```

## Running Pre-commit Hooks

We use pre-commit hooks to ensure code quality. To run them manually:

```bash
poetry run pre-commit run --all-files
```

## Running the Application

To start the application:

```bash
poetry run python main.py
```

## Development Tools

- **Poetry**: Dependency management and packaging
- **pre-commit**: Git hooks for code quality checks

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Run pre-commit hooks
4. Submit a pull request

## License

[Add your license information here]