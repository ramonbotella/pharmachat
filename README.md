# PharmaChat

PharmaChat is a Python-based application that allows users to query a local language model (LLM) about specific medicaments using their leaflets as context. The application scrapes the leaflet information from the CIMA API and uses the Ollama local LLM to provide answers to user questions.

## Features

- Scrape medicament leaflets from the CIMA API.
- Query a local LLM (Ollama) with questions about medicaments.
- Command-line interface (CLI) for easy interaction.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/ramonbotella/pharmachat.git
    cd pharmachat
    ```

2. **Install pharmachat and dependencies using setup_repo.sh script:**

    ```sh
    ./setup_repo.sh
    ```

    This script will install the project dependencies using Poetry and set up the pre-commit hooks."



## Usage

### Command-Line Interface (CLI)

You can use the CLI to ask questions about specific medicaments.

```sh
pharmachat pharma_assistant <medicament_name> <question>
```

## Project Structure

Let us review PharmaChat's folder structure with a brief description of every item.

    ├── model_files                     <- Folder to store the model files for the custimized LLM's.
    ├── pharmachat                      <- Main package folder.
    │   ├──data                         <- Data ETL package folder.
    │   │    └── leaflet_scrapping.py   <- Contains the function to scrape medicament leaflets from the CIMA API.
    │   ├── ml                          <- Machine learning packege folder.
    │   │    └── ollama_interface.py    <- Defines the interface to interact with the Ollama local LLM.
    │   ├── cli                         <- Command-line interface pacakge folder.
    │   │    └── ask_ollama.py          <- CLI to ask Ollama a question about a specific medicament.
    │   ├── __init__.py                 <- Initializes the package and sets the version.
    ├── .gitignore                      <- Generic .gitignore file.
    ├── LICENSE                         <- Project's license file.
    ├── pyproject.toml                  <- Multi-purpose configuration file used by Poetry and several development utilities.
    ├── poetry.lock                     <- Dependency lock file generated by poetry. It should be in version control!
    ├── README.md                       <- The project's README file (which you are currently reading).
## Configuration

### Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality. To set up the pre-commit hooks, run:

```sh
pre-commit install
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Authors

- Ramon Botella Nieto <rbnieto@gmail.com>
