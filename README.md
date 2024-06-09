# OpenWiz CLI - PyPI

## Introduction

The **OpenWiz CLI** stands as a robust command-line utility engineered to leverage the OpenAI API's capabilities in generating code snippets based on user inputs. Its primary objective is to empower developers by furnishing code suggestions and templates directly within their development environment, thereby amplifying coding productivity. This CLI additionally encompasses features for managing configurations, saving and loading sessions, and efficiently handling the generated code.

## Key Features

### 1. Code Generation
The CLI facilitates the creation of code snippets tailored to specific requirements through interactions with the OpenAI API.

### 2. Code Persistence
Developers can seamlessly save the generated code directly to specified files, streamlining the workflow and enabling easy access to previously generated code.

### 3. Session Management
The tool allows for saving and loading sessions, enabling developers to preserve the current state of prompts and generated code for future reference and continuation.

### 4. Configuration Handling
Effortlessly configure the OpenAI API key and other settings to ensure smooth integration and operation of the CLI.

## Installation Guide

### Prerequisites
- Python 3.7 or later
- OpenAI API key

### Developer Setup

1. **Clone the Repository**: Obtain the source code by cloning the project repository from GitHub.
    ```bash
    git clone https://github.com/basith-ahmed/openwiz.git
    cd openwiz
    ```

2. **Virtual Environment Setup**: Create a virtual environment to isolate dependencies and install necessary packages.
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **API Key Configuration**: Configure your OpenAI API key to enable interaction with the OpenWiz CLI.
    ```bash
    python src\cli.py configure
    ```

## Usage Instructions

### 1. Configuration
Before utilizing the package functionalities, it's imperative to configure it with your OpenAI API key.
```bash
python src\cli.py configure
```
**Explanation:** This command prompts the user to input their OpenAI API key for authentication.

### 2. Code Generation
Generate code snippets based on textual prompts using the OpenAI API.
```bash
python src\cli.py generate "Create a Python function to add two numbers"
```
**Sample Output:**
```
Generated Code:
def add(a, b):
    return a + b
```
**Explanation:** This command generates a Python function to add two numbers based on the provided prompt.

### 3. Saving Generated Code
Save the generated code to a specified file for future reference.
```bash
python src\cli.py generate "Create a Python function to subtract two numbers" --file-name subtract.py
```
**Sample Output:**
```
Generated Code:
def subtract(a, b):
    return a - b

> Code saved to subtract.py
```
**Explanation:** This command generates a Python function to subtract two numbers and saves it to a file named `subtract.py`.

### 4. Session Management
Save the current session with a specific name for later retrieval.
```bash
python src\cli.py save --session-name my_session --prompt "Create a Python function to add two numbers"
```
**Sample Output:**
```
Generated Code:
def add(a, b):
    return a + b

> Session my_session saved
```
**Explanation:** This command saves the current session with the provided prompt under the name `my_session`.

### 5. Loading Sessions
Load a previously saved session to resume work from a specific state.
```bash
python src\cli.py load --session-name my_session
```
**Sample Output:**
```
Loaded Session:
{
    "prompt": "Create a Python function to add two numbers",
    "generated_code": "def add(a, b):\n    return a + b"
}
```
**Explanation:** This command loads the session named `my_session`, allowing access to the associated prompt and generated code.
```

### Installation
Install the package from PyPI to streamline integration with existing projects.
```bash
pip install openwiz
```

### Configuration and Usage
Configure the OpenAI API key and utilize the CLI functionalities seamlessly as demonstrated in the previous section.

## Command Reference

| Command   | Description                                              | Options                                                              |
|-----------|----------------------------------------------------------|----------------------------------------------------------------------|
| `generate`| Generate code based on a prompt.                         | `--file-name`: Save the generated code to a specified file.         |
| `save`    | Save the current session with a specified name.          | `--session-name`: Save the generated code as a session to view later.|
| `load`    | Load a previously saved session.                         | `--f`: Load and view all the saved sessions.<br>`--d`: Delete a specific session.<br>`--session-name`: Load a specific session from the saved sessions.|
| `configure` | Configure the OpenAI API key.                           |                                                                      |

## Development Guidelines

### Running Tests
Ensure code integrity by running unit tests.
```bash
pytest tests/
```
**Explanation:** This command executes the unit tests located in the `tests` directory to validate the functionality of the codebase.

### Contribution Workflow
Contribute to the project by following these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Implement changes and add corresponding tests.
4. Commit the changes (`git commit -am 'Add new feature'`).
5. Push the changes to the branch (`git push origin feature-branch`).
6. Create a new Pull Request for review and integration.

## Contributing and Licensing

Contributions to the project are welcome! Refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for detailed guidelines. This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for further information.