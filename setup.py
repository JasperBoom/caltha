#!/usr/bin/env python3

# Copyright (C) 2018 Jasper Boom

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License version 3 as
# published by the Free Software Foundation.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
Imports:
"""
import setuptools

"""
Readme:
"""
with open("README.md", "r") as readme:
    description = readme.read()

"""
Setup:
"""
setuptools.setup(
    name="caltha",
    version="0.7",
    description="A python package to process UMI tagged mixed amplicon\
                 metabarcoding data.",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/JasperBoom/caltha",
    author="Jasper Boom",
    author_email="jboom@infernum.nl",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    keywords="UMI Metabarcoding Amplicon",
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "biopython>=1.78",
        "jellyfish>=0.8.2",
        "numpy>=1.19.2",
        "pandas>=1.1.3",
        "pyfastx>=0.7.0",
        "sre-yield>=1.2"
    ],
    project_urls={
        "Source": "https://github.com/JasperBoom/caltha/tree/master/src",
        "Tracker": "https://github.com/JasperBoom/caltha/issues",
        "Documentation": "https://jasperboom.github.io/caltha/",
    },
    scripts=["src/caltha"],
)

"""
Additional information:
"""
