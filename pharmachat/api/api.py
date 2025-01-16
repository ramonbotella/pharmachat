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
# Created on: 2025-01-16
"""**API package**."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from pharmachat.data.leaflet_scrapping import get_medicament_leaflet
from pharmachat.ml.ollama_interface import OllamaInterface

# Initialize FastAPI app
app = FastAPI()


# Request schema
class PharmaQuery(BaseModel):
    """Request schema for the pharma assistant API endpoint."""

    medicament: str
    question: str


@app.post("/query")
async def pharma_assistant(query: PharmaQuery) -> dict[str, str]:
    """API endpoint to query the Ollama model.

    Args:
        query: PharmaQuery - The request body with the medicament and question.

    Returns:
        response: str - The response from the Ollama model.
    """
    medicament = query.medicament
    question = query.question

    # Get the leaflet text for the medicament
    leaflet = get_medicament_leaflet(medicament)
    if not leaflet:
        raise HTTPException(
            status_code=404, detail=f"Leaflet not found for medicament '{medicament}'."
        )

    # Initialize the Ollama interface and get response
    ollama = OllamaInterface()
    response = ollama.query_ollama(question, leaflet)
    return {"response": response}
