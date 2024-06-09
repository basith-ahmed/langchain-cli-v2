# LangChain CLI - PyPI

## Overview
The **LangChain CLI** is a powerful command-line tool that leverages the OpenAI API to generate code snippets based on user prompts. It is designed to assist developers by providing code suggestions and templates, making the coding process more efficient. The CLI also offers functionalities to save and load sessions, manage configurations, and handle generated code effectively.

## Features
- **Generate Code**: Create code snippets based on textual prompts using the OpenAI API.
- **Save Sessions**: Save the current state of your prompts and generated code for later use.
- **Load Sessions**: Load previously saved sessions to continue working seamlessly.
- **Save Generated Code**: Directly save generated code to specified files.
- **Configuration Management**: Easily configure your OpenAI API key and other settings.

## Installation

### Prerequisites
- Python 3.7 or higher
- OpenAI API key

### Steps - For Developers

1. **Clone the repository**:
    ```bash
    git clone https://github.com/basith-ahmed/openwiz.git
    cd openwiz
    ```
2. **Start a virtual environment**:
    ```cmd
    python -m venv venv
    ```
3. **Start a virtual environment**:
    ```cmd
    .\\venv\\Scripts\\activate
    ```
4. **Install the required packages**:
    ```cmd
    pip install -r requirements.txt
    ```
5. **Configure your OpenAI API key**:
    ```cmd
    python src\\cli.py configure
    ```

## Usage - Repo Clone

### Configure API Key
Configure the OpenAI API key.

```cmd
python src\\cli.py configure
```

**Output:**
```
Enter your OpenAI API key: <your_api_key>
```

### Generate Code
Generate code based on a prompt.

```cmd
python src\\cli.py generate "Create a Python function to add two numbers"
```

**Sample Output:**
```
Generated Code:
def add(a, b):
    return a + b
```

### Save Generated Code to a File
Generate code and save it to a file.

```cmd
python src\\cli.py generate "Create a Python function to subtract two numbers" --file-name subtract.py
```

**Sample Output:**
```
Generated Code:
def subtract(a, b):
    return a - b

> Code saved to subtract.py
```

### Save Session
Save the current session with a specific name.

```cmd
python src\\cli.py save --session-name my_session --prompt "Create a Python function to add two numbers"
```

**Sample Output:**
```
Generated Code:
def add(a, b):
    return a + b

> Session my_session saved
```

### Load Session
Load a previously saved session.

```cmd
python src\\cli.py load --session-name my_session
```

**Sample Output:**
```
Loaded Session:
{
    "prompt": "Create a Python function to add two numbers",
    "generated_code": "def add(a, b):\n    return a + b"
}
```


## Usage - PyPI Package
### Install Package
```cmd
pip install openwiz
```

### Configure API Key
Configure the OpenAI API key.

```cmd
owc configure
```

**Output:**
```
Enter your OpenAI API key: <your_api_key>
```

### Generate Code
Generate code based on a prompt.

```cmd
owc generate "Create a Python function to add two numbers"
```

**Sample Output:**
```
Generated Code:
def add(a, b):
    return a + b
```

### Save Generated Code to a File
Generate code and save it to a file.

```cmd
owc generate "Create a Python function to subtract two numbers" --file-name subtract.py
```

**Sample Output:**
```
Generated Code:
def subtract(a, b):
    return a - b

> Code saved to subtract.py
```

### Save Session
Save the current session with a specific name.

```cmd
owc save --session-name my_session --prompt "Create a Python function to add two numbers"
```

**Sample Output:**
```
Generated Code:
def add(a, b):
    return a + b

> Session my_session saved
```

### Load Session
Load a previously saved session.

```cmd
owc load --session-name my_session
```

**Sample Output:**
```
Loaded Session:
{
    "prompt": "Create a Python function to add two numbers",
    "generated_code": "def add(a, b):\n    return a + b"
}
```


## Command Reference

### `generate`
Generate code based on a prompt.

**Options**:
- `--file-name`: Save the generated code to a specified file.

### `save`
Save the current session with a specified name.
**Options**:
- `--session-name`: Save the generated code as a session to view later.

### `load`
Load a previously saved session.
**Options**:
- `--f`: Load and view all the saved sessions.
- `--d`: Delete a specific session.
- `--session-name`: Load the a specific session from the saved sessions.

### `configure`
Configure the OpenAI API key.

## Development

### Running Tests
To run the unit tests:

```cmd
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
