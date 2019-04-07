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

from PIL import Image, ImageDraw
import pygments.formatters.img
import witchhazel

import wallart.gfx


def _get_minimum_window_width(font_name, font_size):
    font_manager = pygments.formatters.img.FontManager(
        font_name, font_size)

    font = font_manager.get_font(False, False)

    width, height = font.getsize(
        text="=" * 80)

    return width


def draw_window(contents: Image, padding: int = 20) -> Image:
    # Create a new blank image to draw the window frame and code onto.
    min_width = _get_minimum_window_width("Roboto Mono", font_size=32)

    window_width = max(min_width, contents.width)
    window_img = Image.new(
        mode="RGBA",
        size=(window_width + padding * 2, contents.height + padding * 2))
    window_img_draw = ImageDraw.ImageDraw(window_img)

    # Draw the window frame
    wallart.gfx.rounded_rectangle(
        window_img_draw,
        (0, 0, window_img.width, window_img.height),
        radius=20,
        fill=witchhazel.WitchHazelStyle.background_color)

    # Paste in the generated code image.
    window_img.paste(contents, box=(padding, padding))

    # Generate the drop shadow
    final_image = wallart.gfx.drop_shadow(
        window_img,
        padding=120,
        shadow_color=(0, 0, 0, 180),
        offset=(5, 20),
    )

    return final_image
