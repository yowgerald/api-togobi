""" The code is importing necessary modules and classes for the code to work properly."""
import requests

from ai21.base import AI21


class TaskSpecific(AI21):
    """The class TaskSpecific is a subclass of the AI21 class."""

    def contextual_answer(self, context: str, question: str):
        """
        The `contextual_answer` function sends a POST request to an AI21 API endpoint
        to get an answer to a given question based on a given context.
        """
        url = "https://api.ai21.com/studio/v1/experimental/answer"

        payload = {"context": context, "question": question}
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": "Bearer " + self.api_key,
        }

        response = requests.post(url, json=payload, headers=headers, timeout=10)
        return response
