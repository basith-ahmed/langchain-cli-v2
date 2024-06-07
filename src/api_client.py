import openai
from src.logger import Logger

class APIClient:
    def __init__(self, api_key, logger: Logger):
        self.api_key = api_key
        self.logger = logger
        openai.api_key = self.api_key

    def generate_code(self, prompt):
        try:
            message = openai.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": "Generate code for the following prompt and only return the code:\n\n" + prompt,
                    }
                ],
                model="gpt-3.5-turbo",
            )
            # return message.choices[0].text.strip()
            # message = {
            #     "id": "cmpl-5hR1xyzxyzxyz",
            #     "object": "text_completion",
            #     "created": 1616620981,
            #     "model": "text-davinci-003",
            #     "choices": [
            #         {
            #         "text": "def fibonacci(n):\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return fibonacci(n-1) + fibonacci(n-2)\n\nprint('Fibonacci sequence:')\nfor i in range(10):\n    print(fibonacci(i))",
            #         "index": 0,
            #         "finish_reason": "stop"
            #         }
            #     ],
            #     "usage": {
            #         "prompt_tokens": 5,
            #         "completion_tokens": 7,
            #         "total_tokens": 12
            #     }
            # }
            return message['choices'][0]['text']
        except Exception as e:
            print(f"An error occurred: {e}")
            return None