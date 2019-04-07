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

from typing import Tuple, Any

from PIL import Image, ImageDraw, ImageFilter


def rounded_rectangle(
        draw: ImageDraw, box: Tuple[int, int, int, int],
        radius: int,
        fill: Any = None,
        outline: Any = None) -> None:
    """Draw a rounded rectangle on the given image."""
    x1, y1, x2, y2 = box

    draw.rectangle(
        (x1 + radius, y1, x2 - radius, y2),
        fill=fill,
        outline=outline
    )

    draw.rectangle(
        (x1, y1 + radius, x2, y2 - radius),
        fill=fill,
        outline=outline
    )

    diameter = radius * 2

    draw.pieslice(
        (x1, y1, x1 + diameter, y1 + diameter),
        start=180,
        end=270,
        fill=fill,
        outline=outline
    )
    draw.pieslice(
        (x2 - diameter, y1, x2, y1 + diameter),
        start=270,
        end=360,
        fill=fill,
        outline=outline
    )
    draw.pieslice(
        (x2 - diameter, y2 - diameter, x2, y2),
        start=0,
        end=90,
        fill=fill,
        outline=outline
    )
    draw.pieslice(
        (x1, y2 - diameter, x1 + diameter, y2),
        start=90,
        end=180,
        fill=fill,
        outline=outline
    )


def drop_shadow(
        src_image: Image,
        padding: int,
        shadow_color: Any,
        radius: int = 20,
        offset: Tuple[int, int] = (0, 0)):

    # Create a new image
    shadow_img = Image.new(
        mode="RGBA",
        size=(src_image.width + padding * 2, src_image.height + padding * 2))

    draw = ImageDraw.ImageDraw(shadow_img)

    # Draw a colored rectangle.
    box = (
        padding + offset[0],
        padding + offset[1],
        shadow_img.width - padding + offset[0],
        shadow_img.height - padding + offset[1]
    )

    draw.rectangle(
        box,
        fill=shadow_color,
        outline=None
    )

    # Repeatedly apply the blur filter.
    for _ in range(10):
        shadow_img = shadow_img.filter(ImageFilter.BoxBlur(20))

    # Paste the starting image on top of the new drop shadow.
    shadow_img.alpha_composite(src_image, dest=(padding, padding))

    return shadow_img
