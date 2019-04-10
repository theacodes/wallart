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

"""Helpers for loading iterm2 color schemes."""

import dataclasses
import itertools
from typing import Tuple

import xml.etree.ElementTree


def _grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def _xml_dict_to_dict(elem):
    """Transforms XML that looks like this::

            <dict>
                <key>Blue Component</key>
                <real>0.0</real>
                <key>Green Component</key>
                <real>0.0</real>
                <key>Red Component</key>
                <real>0.0</real>
            </dict>

    to Python::

        {
            "Blue Component": "0.0",
            "Green Component": "0.0",
            "Red Component": "0.0",
        }

    Recursively.
    """
    result = {}

    for key, value in _grouper(elem.findall("*"), 2):
        if value.tag == "dict":
            value = _xml_dict_to_dict(value)
        else:
            value = value.text
        result[key.text] = value

    return result


ColorType = Tuple[int, int, int]
default_color = (0, 0, 0)


@dataclasses.dataclass
class ITermColors:
    ansi_0_color: ColorType = default_color
    ansi_1_color: ColorType = default_color
    ansi_2_color: ColorType = default_color
    ansi_3_color: ColorType = default_color
    ansi_4_color: ColorType = default_color
    ansi_5_color: ColorType = default_color
    ansi_6_color: ColorType = default_color
    ansi_7_color: ColorType = default_color
    ansi_8_color: ColorType = default_color
    ansi_9_color: ColorType = default_color
    ansi_10_color: ColorType = default_color
    ansi_11_color: ColorType = default_color
    ansi_12_color: ColorType = default_color
    ansi_13_color: ColorType = default_color
    ansi_14_color: ColorType = default_color
    ansi_15_color: ColorType = default_color
    background_color: ColorType = default_color
    bold_color: ColorType = default_color
    cursor_color: ColorType = default_color
    cursor_text_color: ColorType = default_color
    foreground_color: ColorType = default_color
    selected_text_color: ColorType = default_color
    selection_color: ColorType = default_color

    def escape_code_to_color(self, code: int):
        if 30 <= code <= 37:
            code = code - 30
        elif 90 <= code <= 97:
            code = code - 90 + 8
        elif 40 <= code <= 47:
            code = code - 40
        elif 100 <= code <= 107:
            code = code - 100 + 8

        return getattr(self, f"ansi_{code}_color")


def load(data: str):
    et = xml.etree.ElementTree.fromstring(data)

    # First dict tag has all of the keys and values.
    settings = _xml_dict_to_dict(et.find("dict"))

    colors = ITermColors()

    for attr in dir(colors):
        if attr.startswith("_") or attr in ("escape_code_to_color",):
            continue

        name = attr.replace("_", " ").title()
        xml_color = settings[name]

        setattr(colors, attr, (
            int(255 * float(xml_color["Red Component"])),
            int(255 * float(xml_color["Green Component"])),
            int(255 * float(xml_color["Blue Component"])),
        ))

    return colors
