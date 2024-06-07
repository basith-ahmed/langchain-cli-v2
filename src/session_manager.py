import json
from src.logger import Logger
import os

class SessionManager:
    def __init__(self, logger: Logger):
        self.logger = logger

    def save_session(self, session_name, prompt, generated_code):
        # Ensure the directory exists
        os.makedirs('sessions', exist_ok=True)
        
        # Prepare the session data to be saved
        session_data = {
            'prompt': prompt,
            'generated_code': generated_code
        }
        
        # Attempt to save the session data to a JSON file
        try:
            with open(f"sessions/{session_name}.json", "w") as f:
                json.dump(session_data, f)
            self.logger.log(f"Session '{session_name}' saved.")
        except Exception as e:
            self.logger.log(f"Error saving session '{session_name}': {str(e)}")
            raise

    def load_session(self, session_name):
        with open(f"sessions/{session_name}.json", "r") as f:
            session_data = json.load(f)
        self.logger.log(f"Session {session_name} loaded")
        return session_data
