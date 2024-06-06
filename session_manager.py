import json
from logger import Logger

class SessionManager:
    def __init__(self, logger: Logger):
        self.logger = logger

    def save_session(self, session_name, prompt, generated_code):
        session_data = {
            "prompt": prompt,
            "generated_code": generated_code
        }
        with open(f"sessions/{session_name}.json", "w") as f:
            json.dump(session_data, f)
        self.logger.log(f"Session {session_name} saved")

    def load_session(self, session_name):
        with open(f"sessions/{session_name}.json", "r") as f:
            session_data = json.load(f)
        self.logger.log(f"Session {session_name} loaded")
        return session_data
