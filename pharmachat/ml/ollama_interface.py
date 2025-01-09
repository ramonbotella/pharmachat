# MIT License
#
# Copyright (c) 2025 Ramon Botella Nieto
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Author: Ramon Botella Nieto
# Email: rbnieto@gmail.com
# Created on: 2025-01-09
"""Interface to interact with the Ollama local LLM."""

import json

import requests
from loguru import logger

from pharmachat.core import config


class OllamaInterface:
    """Interface to interact with the Ollama local LLM."""

    def __init__(self, model_name=config.LLM_MODEL):
        """Initializes the OllamaInterface class.

        Args:
            model_name (str): The name of the Ollama model to use.
        """
        self.model_name = model_name
        self.api_url = config.API_ENDPOINT
        self.session = requests.Session()
        self.headers = {
            "Content-Type": "application/json",
        }

    def query_ollama(self, prompt: str, context: str) -> str:
        """Queries the Ollama local LLM with a given prompt and context.

        Parameters:
            model (str): The name of the Ollama model to use.
            prompt (str): The user question or prompt.
            context (str): The pharmaceutical leaflet text to use as context.

        Returns:
            str: The response from the model.
        """
        output = ""
        payload = {
            "model": self.model_name,
            "prompt": f"Context:\n{context}\n\nQuestion: {prompt}\n\nAnswer:",
        }
        with self.session.post(self.api_url, json=payload, stream=True) as response:
            if response.status_code == 200:
                for line in response.iter_lines():
                    if line:
                        j = json.loads(line.decode("utf-8"))
                        output += j.get("response", "No response from the model.")
                        if j.get("done", True):
                            break
            else:
                logger.error(f"Error querying the model: {response.text}")

        return output.strip()
