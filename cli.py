import argparse
from api_client import APIClient
from session_manager import SessionManager
from code_storage import CodeStorage
from config_manager import ConfigManager
from logger import Logger
from error_handler import ErrorHandler

def main():
    parser = argparse.ArgumentParser(description="CLI-based Coding Co-Pilot")
    parser.add_argument("command", choices=["generate-code", "save-session", "load-session", "configure"], help="Command to execute")
    parser.add_argument("prompt", type=str, nargs="?", help="The prompt to generate code for")
    parser.add_argument("--session-name", type=str, help="Name of the session to save/load")
    parser.add_argument("--file-name", type=str, help="File name to save generated code")
    args = parser.parse_args()

    logger = Logger()
    config_manager = ConfigManager()
    api_client = APIClient(config_manager.get_api_key(), logger)
    session_manager = SessionManager(logger)
    code_storage = CodeStorage(logger)
    error_handler = ErrorHandler(logger)

    try:
        if args.command == "generate-code" and args.prompt:
            generated_code = api_client.generate_code(args.prompt)
            print("Generated Code:\n", generated_code)
            if args.file_name:
                code_storage.save_code(args.file_name, generated_code)
        elif args.command == "save-session" and args.session_name and args.prompt:
            generated_code = api_client.generate_code(args.prompt)
            session_manager.save_session(args.session_name, args.prompt, generated_code)
            print("Session saved successfully.")
        elif args.command == "load-session" and args.session_name:
            session = session_manager.load_session(args.session_name)
            print("Loaded Session:\n", session)
        elif args.command == "configure":
            config_manager.configure()
        else:
            parser.print_help()
    except Exception as e:
        error_handler.handle(e)

if __name__ == "__main__":
    main()
