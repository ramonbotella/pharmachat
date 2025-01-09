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
"""Leaflet scrapping module."""

import requests
from bs4 import BeautifulSoup

from pharmachat.core import config


def get_medicament_leaflet(medicament_name: str) -> str:
    """Get the leaflet of a medicament by its name.

    Args:
        medicament_name (str): The name of the medicament.

    Returns:
        str: The leaflet text.
    """
    # Base URL for the CIMA API

    try:
        # Step 1: Search for medicament matching the name
        search_url = f"{config.BASE_SEARCH_URL}/rest/medicamentos"
        response = requests.get(search_url, params={"nombre": medicament_name})

        if response.status_code != 200:
            return (
                f"Error: Unable to fetch medicament. Status code {response.status_code}"
            )

        medicament = response.json()

        if not medicament:
            return f"No medicament found for '{medicament_name}'."

        # Step 2: Take the first matching medicament and get its registration number
        first_medicament = medicament["resultados"][0]
        registration_number = first_medicament.get("nregistro")

        if not registration_number:
            return (
                f"No registration number found for the medicament '{medicament_name}'."
            )

        # Step 3: Fetch the leaflet (prospectus) using the registration number
        leaflet_url = f"{config.BASE_LEAFLET_URL}{registration_number}/P_{registration_number}.html"
        leaflet_response = requests.get(leaflet_url)

        if leaflet_response.status_code != 200:
            return f"Error: Unable to fetch leaflet. Status code {leaflet_response.status_code}"

        # Parse the HTML content of the leaflet
        soup = BeautifulSoup(leaflet_response.text, "html.parser")
        leaflet_text = soup.get_text(strip=True)  # Extract only the text content

        return leaflet_text

    except Exception as e:
        return f"An error occurred: {str(e)}"


# Example usage:
if __name__ == "__main__":
    drug_name = "enantyum"
    leaflet = get_medicament_leaflet(drug_name)
    print(leaflet)
