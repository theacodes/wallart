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

from PIL import Image
import pygments
import pygments.lexers
import pygments.formatters
import witchhazel


def highlight(code: str, style: str) -> Image:
    # https://github.com/theacodes/witchhazel/issues/2
    if style == "witchhazel":
        style = witchhazel.WitchHazelStyle

    formatter = pygments.formatters.ImageFormatter(
        style=style,
        line_pad=2,
        font_name="Roboto Mono",
        font_size=32,
        line_numbers=False,
        hl_lines=[],
        hl_color=None,
    )

    pyg_image_data = pygments.highlight(
        code,
        pygments.lexers.Python3Lexer(),
        formatter)

    return Image.open(io.BytesIO(pyg_image_data))
