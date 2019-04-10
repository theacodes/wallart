# Copyright 2019 Alethea Katherine Flowers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import pkgutil

from PIL import Image
import pygments
import pygments.lexers
import pygments.formatters
import pygments.style
import witchhazel

import wallart.ansi
import wallart.iterm


def highlight(code: str, ansi: str, style: str, term_theme: str) -> Image:
    # https://github.com/theacodes/witchhazel/issues/2
    if style == "witchhazel":
        style = witchhazel.WitchHazelStyle

    if not ansi:
        formatter_cls = pygments.formatters.ImageFormatter
    else:
        formatter_cls = wallart.ansi.ConsoleImageFormatter

    formatter = formatter_cls(
        style=style,
        line_pad=2,
        font_name="Roboto Mono Emoji",
        font_size=32,
        line_numbers=False,
        hl_lines=[],
        hl_color=None,
    )

    if not ansi:
        lexer = pygments.lexers.guess_lexer(code)

        # Force the Python 3 lexer.
        if isinstance(lexer, pygments.lexers.PythonLexer):
            lexer = pygments.lexers.Python3Lexer()

    else:
        if not term_theme:
            term_theme = wallart.iterm.load(
                pkgutil.get_data("wallart", "Dracula.itermcolors"))
        else:
            with open(term_theme, "r") as fh:
                term_theme = wallart.iterm.load(fh.read())

        lexer = wallart.ansi.ConsoleOutputLexer(theme=term_theme)

    pyg_image_data = pygments.highlight(
        code,
        lexer,
        formatter)

    return Image.open(io.BytesIO(pyg_image_data))
