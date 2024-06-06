import yaml

class ConfigManager:
    def __init__(self):
        self.config_file = "config/user_config.yaml"
        self.load_config()

    def load_config(self):
        with open(self.config_file, "r") as f:
            self.config = yaml.safe_load(f)

    def get_api_key(self):
        return self.config["api_key"]

    def configure(self):
        api_key = input("Enter your OpenAI API key: ")
        self.config["api_key"] = api_key
        with open(self.config_file, "w") as f:
            yaml.safe_dump(self.config, f)
