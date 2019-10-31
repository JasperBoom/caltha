#!/usr/bin/env python3

# Author: Jasper Boom

# Prequisites:
# - conda install -c bioconda vsearch=2.14.1

# Imports
import setuptools

with open("README.md", "r") as oisReadme:
    strDescription = oisReadme.read()

setuptools.setup(
    name="caltha",
    version="0.4",
    description="A python package to process UMI tagged mixed amplicon metabarcoding data.",
    long_description=strDescription,
    long_description_content_type="text/markdown",
    url="https://github.com/JasperBoom/caltha",
    author="Jasper Boom",
    author_email="jboom@infernum.nl",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ],
    keywords="UMI Metabarcoding",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "pandas>=0.25.1"
    ],
    project_urls={
        "Source": "https://github.com/JasperBoom/caltha/tree/master/src",
        "Tracker": "https://github.com/JasperBoom/caltha/issues",
        "Documentation": "https://jasperboom.github.io/caltha/"
    },
    scripts=["src/caltha"]
)
