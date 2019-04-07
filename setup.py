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

from setuptools import setup


long_description = open("README.md", "r", encoding="utf-8").read()


setup(
    name="wallart",
    version="2019.4.7",
    description="Make pretty pictures out of code or console output.",
    long_description=long_description,
    url="https://github.com/theacodes/wallart",
    author="Alethea Katherine Flowers",
    author_email="me@thea.codes",
    license="Apache Software License",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: Unix",
    ],
    keywords="code formatting",
    packages=["wallart"],
    include_package_data=True,
    install_requires=[
        "pygments>=2.0.0",
        "pillow>=6.0.0",
        "witchhazel",
        "click>=7.0"
    ],
    entry_points={
        "console_scripts": [
            "wallart=wallart.__main__:main",
        ]
    },
    project_urls={
        "Documentation": "https://nox.thea.codes",
        "Source Code": "https://github.com/theacodes/nox",
        "Bug Tracker": "https://github.com/theacodes/nox/issues",
    },
    python_requires=">=3.6",
)
