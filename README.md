<a href="https://github.com/new?template_name=foundation&template_owner=scuffi">
  <img src="https://img.shields.io/badge/use%20template-light_green?style=for-the-badge&logo=github">
</a>

# Python Base Project

This template serves as an essential foundation for Python projects, offering a streamlined configuration and setup. Designed to expedite the initiation of new projects, it provides a minimal yet comprehensive template, significantly reducing the time required for project commencement.

This template is designed to be versatile across various Python project types (such as APIs, scheduled services, etc.), without favoring any specific use case. Its focus lies in enhancing code quality and offering utility functions to streamline and expedite repetitive tasks.

*Note: This project will have stuff missing, it may not fit requirements to be a base for every project, but it's good enough for me :D*

## How to use

To use this template for a project simply click the use template button above. [(Or if you're lazy just click here)](https://github.com/new?template_name=foundation&template_owner=scuffi)

The configure your new project as you want, then open the new project in your chosen editor.

To setup your environment, create a virtual environment using your chosen Python version, then run:

```bash
make setup-env
```

This will install all the project dependencies, and set up the pre-commit hooks automatically.

## Features

This template has features to make jumping into development a little faster, for example:

- Basic project structure of folders and config files
- Pre-commit hooks for everything you'll need to ensure code quality:
  - `isort` -> Python import sorting
  - `talisman` -> Check for private keys/secrets in code
  - `ruff` -> Python linting & formatting
  - `bandit` -> Check for common security issues
  - `clean-dotenv` -> Create a `.env.example` file containing all keys from private `.env`
  - `mypy` -> Static type checking
- Makefile providing utility commands to speed up development
- Bumpversion to make updating project versions swift and easy
- pip-compile for better dependencies
- Dependabot setup for dependency updates
- [TODO] Devcontainer configuration for all-in-one VSCode environment
- [TODO] Workflow configurations

### Makefile

The Make commands are as follows (Use in format `make {command}`):

- `setup-env` -> Setup the default environment (only needs to be ran once)
- `lint` -> Run all pre-commit checks over the project
- `format` -> Format the project using Ruff formatter
- `test` -> Run all tests in the `/tests` directory
- `compile-requirements` & `freeze` -> Use pip-compile to freeze the requirements into `requirements.txt`
- `build` -> Build the `docker-compose.yml` images
- `up` -> Spin up the `docker-compose.yml` containers
- `docker` -> Build & spin up the `docker-compose.yml` containers

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update documentation as appropriate.

## License

[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)
