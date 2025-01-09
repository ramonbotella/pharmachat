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
"""**Environment setup package for the project**."""

import yaml
from dotenv import load_dotenv, set_key


def load_config():
    """Load the configuration file."""
    with open("pharmachat/config/config.yaml") as file:
        config = yaml.safe_load(file)
    return config


def write_env_file(config):
    """Write the configuration to the .env file."""
    env_file = ".env"
    for key, value in config.items():
        set_key(env_file, key, str(value))


if __name__ == "__main__":
    config = load_config()
    write_env_file(config)
    load_dotenv()  # Load the environment variables to the current session
