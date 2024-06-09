# OpenWiz CLI - PyPI

## Overview
The **OpenWiz CLI** is a powerful command-line tool that utilizes the OpenAI API to generate code snippets based on user prompts. It is designed to assist developers by providing code suggestions and templates directly into their development environment, thereby enhancing coding efficiency. The CLI also offers functionalities to save and load sessions, manage configurations, and handle generated code effectively.

## Features
- **Generate Code**: Create code snippets based on textual prompts using the OpenAI API.
- **Save Generated Code**: Directly save generated code to specified files.
- **Save and Load Sessions**: Save the current state of your prompts and generated code for later use and seamlessly continue working with previously saved sessions.
- **Configuration Management**: Easily configure your OpenAI API key and other settings.

## Installation

### Prerequisites
- Python 3.7 or higher
- OpenAI API key

### Steps for Developers

1. Clone the repository:
    ```bash
    git clone https://github.com/basith-ahmed/openwiz.git
    cd openwiz
    ```

2. Set up a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Configure your OpenAI API key:
    ```bash
    python src\cli.py configure
    ```

## Usage

1. **Configure API Key**:
Before using the package, you need to configure it with your openai api key.
```bash
python src\cli.py configure
```
**Output:**
```
Enter your OpenAI API key: <your_api_key>
```

2. **Generate Code**
```bash
python src\cli.py generate "Create a Python function to add two numbers"
```
**Sample Output:**
```
Generated Code:
def add(a, b):
    return a + b
```

**Save Generated Code to a File**
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

**Save Session**
Save the current session with a specific name.

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

**Load Session**
Load a previously saved session.

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

## Usage with PyPI Package
**Install Package**
```bash
pip install openwiz
```

**Configure API Key**
Configure the OpenAI API key.

```bash
owc configure
```

**Generate Code**
Generate code based on a prompt.

```bash
owc generate "Create a Python function to add two numbers"
```

**Save Generated Code to a File**
Generate code and save it to a file.

```bash
owc generate "Create a Python function to subtract two numbers" --file-name subtract.py
```

**Save Session**
Save the current session with a session name.

```bash
owc save --session-name my_session --prompt "Create a Python function to add two numbers"
```

**Load Session**
Load a previously saved session.

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


## Development

**Running Tests*
To run the unit tests:

```bash
pytest tests/
```
**Output:**
```
============================= test session starts =============================
collected 8 items

tests/test_api_client.py ....                                              [ 50%]
tests/test_code_storage.py .                                               [ 62%]
tests/test_config_manager.py .                                             [ 75%]
tests/test_error_handler.py .                                              [ 87%]
tests/test_logger.py .                                                     [100%]

============================= 8 passed in 0.45s ==============================
```

### Adding New Features or Fixes
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and add tests for them.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Contributing

We welcome contributions! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.