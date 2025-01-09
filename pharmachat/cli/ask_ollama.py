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

"""CLI to ask Ollama a question."""

from loguru import logger
from typer import Argument, Typer

from pharmachat.data.leaflet_scrapping import get_medicament_leaflet
from pharmachat.ml.ollama_interface import OllamaInterface

app = Typer()


@app.command(help="Ask Ollama a question about a specific medicament.")
def pharma_assistant(
    medicament: str = Argument(..., help="Exact name of the medicament"),
    question: str = Argument(..., help="Question to ask Ollama model"),
):
    """CLI to ask Ollama a question.

    This command allows the user to ask a question to the Ollama model
    using the leaflet of a specific medicament as context.

    Parameters:
        model (str): The name of the Ollama model to use.
        medicament (str): The exact name of the medicament to use.
        question (str): The question to ask the Ollama model.
    """
    # Get the leaflet text for the medicament
    leaflet = get_medicament_leaflet(medicament)

    if leaflet:
        # Initialize the Ollama interface
        ollama = OllamaInterface()
        response = ollama.query_ollama(question, leaflet)
        logger.info(response)
    else:
        logger.info(f"Error: Unable to fetch leaflet for '{medicament}'.")


if __name__ == "__main__":
    app()
