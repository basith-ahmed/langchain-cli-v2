import openai
from logger import Logger

class APIClient:
    def __init__(self, api_key, logger: Logger):
        self.api_key = api_key
        self.logger = logger
        openai.api_key = self.api_key

    def generate_code(self, prompt):
        try:
            self.logger.log("Sending prompt to OpenAI API")
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150
            )
            self.logger.log("Received response from OpenAI API")
            return response.choices[0].text.strip()
        except Exception as e:
            self.logger.log(f"Error in API Client: {e}")
            raise
