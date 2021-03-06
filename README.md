# Caltha
A python package for processing UMI tagged mixed amplicon metabarcoding data.

[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Installation
The current version of __Caltha__ requires Python 3.8+.

To install __Caltha__, simply run the pip install command:
```
pip install caltha
```

NOTE: __Caltha__ does require one more dependency which can not be installed
with the __Caltha__ pip or conda package. This dependency is
[vsearch](https://github.com/torognes/vsearch) (2.14.2).  
Executing the following conda install command should install the dependency.
```
conda install -c bioconda vsearch
```

## How to run
__Caltha__ can be run directly from the command line.
```
usage: caltha [-h] [-v] [-i FLINPUT] [-t FLTABULAR] [-z FLPREZIP] [-b FLBLAST]
              [-f STRFORMAT] [-l STRLOCATION] [-a STRANCHOR] [-u INTUMILENGTH]
              [-y FLTIDENTITY] [-c INTABUNDANCE] [-w STRFORWARD]
              [-r STRREVERSE] [-d STRDIRECTORY] [-@ INTTHREADS]

A python package for processing UMI tagged mixed amplicon metabarcoding data.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -i FLINPUT, --input FLINPUT
                        The input fasta/fastq file(s). This can either be a
                        zip archive or a single fasta/fastq file.
  -t FLTABULAR, --tabular FLTABULAR
                        The output tabular zip file.
  -z FLPREZIP, --zip FLPREZIP
                        The pre validation zip file.
  -b FLBLAST, --blast FLBLAST
                        The output blast zip file.
  -f STRFORMAT, --format STRFORMAT
                        The format of the input file
                        [fasta/fastq]. (default: fasta)
  -l STRLOCATION, --location STRLOCATION
                        Search for UMIs at the 5'-end [umi5], 3'-end [umi3] or 
                        at the 5'-end and 3'-end [umidouble]. (default: umi5)
  -a STRANCHOR, --anchor STRANCHOR
                        Which anchor type to use
                        [primer/adapter/zero]. (default: primer)
  -u INTUMILENGTH, --length INTUMILENGTH
                        The length of the UMI sequence. (default: 5)
  -y FLTIDENTITY, --identity FLTIDENTITY
                        The identity percentage with which to perform the
                        validation. (default: 0.97)
  -c INTABUNDANCE, --abundance INTABUNDANCE
                        The minimum abundance of a sequence in order for it
                        to be included during validation. (default: 1)
  -w STRFORWARD, --forward STRFORWARD
                        The 5'-end anchor nucleotides.
  -r STRREVERSE, --reverse STRREVERSE
                        The 3'-end anchor nucleotides.
  -d STRDIRECTORY, --directory STRDIRECTORY
                        The location of the temporary working directory
                        (not created by program). (default: .)
  -@ INTTHREADS, --threads INTTHREADS
                        The number of threads to run Caltha
                        with. (default: number of threads available on system)

This python package requires one extra dependency which can be easily
installed with conda (conda install -c bioconda vsearch=2.14.2).
```

Further documentation can be found [here](https://jasperboom.github.io/caltha/).

## Package links
* [PyPI](https://pypi.org/project/caltha/)

## Source(s)
* __Python Software Foundation__,  
  Python 3.8+. 2019.  
  [Python](https://www.python.org/)
* __Rognes T, Flouri T, Nichols B, Quince C, Mahe F__,  
  VSEARCH: A versatile open source tool for metagenomics.  
  PeerJ. 2016. __doi: 10.7717/peerj.2584__  
  [vsearch](https://github.com/torognes/vsearch)
* __Augspurger T, Ayd W, Bartak C, Battiston P, Cloud P, Garcia M__,  
  Python Data Analysis Library.  
  [Pandas](https://pandas.pydata.org/)
* __Langa L, Willing C, Meyer C, Zijlstra J, Naylor M, Dollenstein Z__,  
  The uncompromising Python code formatter.  
  [Black](https://black.readthedocs.io/en/stable/)
* __Ziadé T, Cordasco I__,  
  Your tool for style guide enforcement.  
  [Flake8](http://flake8.pycqa.org/en/latest/index.html)
* __Sottile A, Struys K, Kuehl C, Finkle M__,  
  A framework for managing and maintaining multi-language pre-commit hooks.  
  [Pre-commit](https://pre-commit.com/)
* __Python Software Foundation__,  
  The Python Package index.  
  [PyPI](https://pypi.org/)
* __Du L__,  
  A lightweight Python C extension for easy access to sequences from plain and
  gzipped fasta/q files.  
  [Pyfastx](https://pyfastx.readthedocs.io/en/latest/)
* __Cock P, Antao T, Chang J, Chapman B, Cox C, Dalke A__,  
  Biopython: freely available Python tools for computational molecular biology
  and bioinformatics.  
  Bioinformatics. 2009; 25(11): 1422-1423. __doi: 10.1093/bioinformatics/btp163__  
  [Biopython](https://biopython.org/)

## Author(s)
* [Jasper Boom](https://github.com/JasperBoom)

## Citation
* __Boom J__, Caltha.  
  GitHub repository: https://github.com/JasperBoom/caltha

```
Copyright (C) 2018 Jasper Boom

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License version 3 as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
```
