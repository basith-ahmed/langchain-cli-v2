# OpenWiz CLI

## Overview
The **OpenWiz CLI** is a powerful command-line tool that utilizes the OpenAI API to generate code snippets based on user prompts. It is designed to assist developers by providing code suggestions and templates directly into their development environment, thereby enhancing coding efficiency. The CLI also offers functionalities to save and load sessions, manage configurations, and handle generated code effectively.

## Features
- **Generate Code**: Create code snippets based on textual prompts using the OpenAI API.
- **Save Generated Code**: Directly save generated code to specified files.
- **Save and Load Sessions**: Save the current state of your prompts and generated code for later use and seamlessly continue working with previously saved sessions.
- **Configuration Management**: Easily configure your OpenAI API key and other settings.

## Installation Guide

### Prerequisites
- Python 3.7 or later
- OpenAI API key

### Developer Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/basith-ahmed/openwiz.git
    cd openwiz
    ```

2. **Virtual Environment Setup**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **API Key Configuration**:
    ```bash
    python src\cli.py configure
    ```

## Usage Instructions

### 1. Configuration
```bash
python src\cli.py configure
```
**Output:**
```
Enter your OpenAI API key: <your_api_key>
```
### 2. Code Generation
```bash
python src\cli.py generate "Create a Python function to add two numbers"
```
**Sample Output:**
```
Generated Code:
def add(a, b):
    return a + b
```

### 3. Saving Generated Code
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

### Installation
Install the package from PyPI to integrate with existing projects.

```bash
pip install openwiz
```
### Configuration and Usage
Configure the OpenAI API key and utilize the CLI functionalities as demonstrated in the previous section.

#### 1. Configuration
```bash
owc configure
```
#### 2. Code Generation
```bash
owc generate "Create a Python function to add two numbers"
```
#### 3. Saving Generated Code
```bash
owc generate "Create a Python function to subtract two numbers" --file-name subtract.py
```
#### 4. Session Management
```bash
owc save --session-name my_session --prompt "Create a Python function to add two numbers"
```
#### 5. Loading Sessions
```bash
owc load --session-name my_session
```

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

## Contributing

We welcome contributions! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.