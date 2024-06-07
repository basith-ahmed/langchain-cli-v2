import openai
from src.logger import Logger

class APIClient:
    def __init__(self, api_key, logger: Logger):
        self.api_key = api_key
        self.logger = logger
        openai.api_key = self.api_key

    def generate_code(self, prompt):
        try:
            # message = openai.chat.completions.create(
            #     messages=[
            #         {
            #             "role": "user",
            #             "content": "Say this is a test",
            #         }
            #     ],
            #     model="gpt-3.5-turbo",
            # )
            # return message.choices[0].text.strip()
            return "Hey this is your response"
        except Exception as e:
            print(f"An error occurred: {e}")
            return None