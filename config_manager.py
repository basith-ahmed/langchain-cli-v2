import yaml
import os

class ConfigManager:
    def __init__(self, config_file='config/user_config.yaml'):
        self.config_file = config_file
        self.config = {}
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            self.create_default_config()
        with open(self.config_file, "r") as f:
            self.config = yaml.safe_load(f)

    def create_default_config(self):
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        default_config = {
            'api_key': ''
        }
        with open(self.config_file, "w") as f:
            yaml.safe_dump(default_config, f)
        print(f"Created default config file at {self.config_file}. Please configure it with your API key.")

    def configure(self):
        api_key = input("Enter your OpenAI API key: ")
        self.config["api_key"] = api_key
        with open(self.config_file, "w") as f:
            yaml.safe_dump(self.config, f)
        print("API key configured successfully.")

    def get_api_key(self):
        return self.config.get('api_key', None)
