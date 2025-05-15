import openai
from .base_provider import BaseAPIProvider
import os
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


class OpenAI_API(BaseAPIProvider):
    MODELS = {
        "gpt-4o": {"name": "GPT-4o", "provider": "OpenAI"},
        "gpt-4o-mini": {"name": "GPT-4o Mini", "provider": "OpenAI"},
        "gpt-3.5-turbo": {"name": "GPT-3.5 Turbo", "provider": "OpenAI"},
    }

    def __init__(self):
        self.api_key = os.environ.get("OPENAI_API_KEY")

    def set_model(self, model_name: str = None):
        # Define your default model here
        DEFAULT_MODEL = "gpt-4o"

        if model_name is None or model_name not in self.MODELS:
            # Log and set the default model
            logger.warning(f"Invalid or missing model name. Falling back to default: {DEFAULT_MODEL}")
            self.current_model = DEFAULT_MODEL
        else:
            self.current_model = model_name

    def get_models(self) -> dict:
        if self.api_key is not None:
            return self.MODELS
        else:
            return {}

    def generate_response(self, prompt: str, system_content: str, temperature=0.7) -> str:
        try:
            self.client = openai.OpenAI(api_key=self.api_key)
            
            # Format the messages
            api_messages = [
                {"role": "system", "content": system_content},
                {"role": "user", "content": prompt}
            ]
            vector_store_ids = [
                "vs_68248bf344f48191afa72cf5bbf1a480"
                ]

            # Use the assistant-style call
            response = self.client.responses.create(
                model=self.current_model,
                input=api_messages,
                temperature=temperature,
                tools=[
                    {"type": "file_search", "vector_store_ids": vector_store_ids}
                ],
                store=True,
            )

            return response.output_text

        except openai.APIConnectionError as e:
            logger.error(f"Server could not be reached: {e.__cause__}")
            raise e
        except openai.RateLimitError as e:
            logger.error(f"A 429 status code was received. {e}")
            raise e
        except openai.AuthenticationError as e:
            logger.error(f"There's an issue with your API key. {e}")
            raise e
        except openai.APIStatusError as e:
            logger.error(f"Another non-200-range status code was received: {e.status_code}")
            raise e
