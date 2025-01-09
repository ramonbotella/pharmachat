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
"""**Configuration package for the project**."""

from pathlib import Path

import yaml
from pydantic_settings import BaseSettings


class GlobalConfig(BaseSettings):
    """Global configuration class for the project."""

    # Define your configuration fields here
    BASE_SEARCH_URL: str
    BASE_LEAFLET_URL: str
    LLM_MODEL: str
    API_ENDPOINT: str

    class Config:
        """Configuration for the GlobalConfig class."""

        env_file = Path(__file__).resolve().parents[3] / ".env"
        env_file_encoding = "utf-8"

    @classmethod
    def from_yaml(cls, yaml_path: Path) -> "GlobalConfig":
        """Load configuration from a YAML file.

        Args:
            yaml_path (Path): Path to the YAML file.

        Returns:
            GlobalConfig: Configuration loaded from the YAML file.
        """
        with open(yaml_path) as file:
            config_data = yaml.safe_load(file)
        return cls(**config_data)


# Load configuration from config.yaml
config_yaml_path = Path(__file__).resolve().parents[2] / "config" / "config.yaml"
config = GlobalConfig.from_yaml(config_yaml_path)
