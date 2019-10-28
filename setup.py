#!/usr/bin/env python3
# Copyright ©2001-2019 Python Software Foundation

# Author: Jasper Boom

# Prequisites:
# - conda install -c bioconda vsearch=2.14.1
# - conda install -c anaconda pandas=0.25.1

# Imports
import setuptools

with open("README.md", "r") as oisReadme:
    strDescription = oisReadme.read()

setuptools.setup(
    name="caltha",
    version="0.1",
    description="A python package to process UMI tagged mixed amplicon metabarcoding data.",
    long_description=strDescription,
    long_description_content_type="text/markdown",
    url="https://github.com/JasperBoom/caltha",
    author="Jasper Boom",
    author_email="jboom@infernum.nl",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ],
    keywords="UMI metabarcoding",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "pandas>=0.25.1"
    ],
    project_urls={
        "Source": "https://github.com/JasperBoom/caltha",
        "Tracker": "https://github.com/JasperBoom/caltha/issues",
        "Documentation": "https://jasperboom.github.io/caltha/"
    },
    scripts=["src/caltha"]
)
