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

"""**Command line interface**.

Basic CLI to implement agora functionalities.

Using `Typer <https://typer.tiangolo.com/>`_ we build a basic
*Command Line Interface* to interact with
``pharmachat``'s main functionalities.

Different sub-commands should be coded in separate files, each
of them with its own app Typer instance, and added to the
main app Typer instance defined here via the ``app.add_typer`` method.

There is a special :func:`.main_callback` which enables the
``--version`` option when there is no subcommand:

.. code-block:: console

   $ pharmachat --version

"""
import sys

import rich
import typer
from rich.panel import Panel
from typer import Option, Typer

from pharmachat import __version__
from pharmachat.cli.ask_ollama import pharma_assistant

app = Typer()
"""Main Typer application.

This is the CLI entrypoint. It has one single ``--version`` option,
defined in :func:`.main_callback`, that can be used to display the
current installed version of ``pharmachat``.

"""


app.command(
    name="pharma-assistant", help="Ask Ollama a question about a specific medicament."
)(pharma_assistant)


@app.callback(invoke_without_command=True, no_args_is_help=True)
def main_callback(version: bool = Option(False, help="Show the package version.")):
    """Pharmachat command line interface."""
    _v = __version__
    _p = sys.platform.capitalize()
    if version is not None:
        rich.print(
            Panel.fit(
                f"pharmachat, version {_v} on {_p}",
                style="bold green",
                title_align="center",
            )
        )


typer_click_object = typer.main.get_command(app)
"""Main Click object derived from the main Typer app."""

if __name__ == "__main__":
    app()
