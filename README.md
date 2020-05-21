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
[Vsearch](https://github.com/torognes/vsearch) (2.14.2).  
Executing the following conda install command should install the dependency.
```
conda install -c bioconda vsearch
```

## How to run
__Caltha__ can be run directly from the command line.
```
usage: caltha [-h] [-v] [-i FISINPUT] [-t FOSTABULAR] [-z FOSPREZIP]
              [-b FOSBLAST] [-f DISFORMAT] [-s DISSEARCH] [-a DISAPPROACH]
              [-u DISUMILENGTH] [-y DISIDENTITY] [-c DISABUNDANCE]
              [-w DISFORWARD] [-r DISREVERSE] [-d FISDIRECTORY]
              [-p DISPROCESSES]

A python package for processing UMI tagged mixed amplicon metabarcoding data.

optional arguments:
  -h, --help            show this help message and exit
  -v, -version          show program's version number and exit
  -i FISINPUT, -input FISINPUT
                        The location of the input fasta/fastq file(s).
  -t FOSTABULAR, -tabular FOSTABULAR
                        The location of the output tabular zip file.
  -z FOSPREZIP, -zip FOSPREZIP
                        The location of the pre validation zip file.
  -b FOSBLAST, -blast FOSBLAST
                        The location of the output blast zip file.
  -f DISFORMAT, -format DISFORMAT
                        The format of the input file
                        [fasta/fastq/zipfasta/zipfastq].
  -s DISSEARCH, -search DISSEARCH
                        Search for UMIs at the 5'-end [umi5], 3'-end [umi3] or
                        at the 5'-end and 3'-end [umidouble]. (default: umi5)
  -a DISAPPROACH, -approach DISAPPROACH
                        Which anchor type to use [primer/adapter/zero].
                        (default: primer)
  -u DISUMILENGTH, -length DISUMILENGTH
                        The length of the UMI sequence.
  -y DISIDENTITY, -identity DISIDENTITY
                        The identity percentage with which to perform the
                        validation. (default: 0.97)
  -c DISABUNDANCE, -abundance DISABUNDANCE
                        The minimum abundance of a sequence in order for it to
                        be included during validation. (default: 1)
  -w DISFORWARD, -forward DISFORWARD
                        The 5'-end anchor nucleotides.
  -r DISREVERSE, -reverse DISREVERSE
                        The 3'-end anchor nucleotides.
  -d FISDIRECTORY, -directory FISDIRECTORY
                        The location of the temporary working directory.
                        (default: .)
  -p DISPROCESSES, -processes DISPROCESSES
                        The number of threads to run Caltha with. (default:
                        number of threads available on system)

This python package requires one extra dependency which can be easily
installed with conda (conda install -c bioconda vsearch).
```

Further documentation can be found [here](https://jasperboom.github.io/caltha/).

## Package links
* [PyPI](https://pypi.org/project/caltha/)

## Source(s)
* __Giardine B, Riemer C, Hardison RC, Burhans R, Elnitski L, Shah P__,  
  Galaxy: A platform for interactive large-scale genome analysis.  
  Genome Research. 2005; 15(10) 1451-1455. __doi: 10.1101/gr.4086505__  
  [Galaxy](https://www.galaxyproject.org/)
* __Python Software Foundation__,  
  Python 3.8+. 2019.  
  [Python](https://www.python.org/)
* __Rognes T, Flouri T, Nichols B, Quince C, Mahe F__,  
  VSEARCH: A versatile open source tool for metagenomics.  
  PeerJ. 2016. __doi: 10.7717/peerj.2584__  
  [Vsearch](https://github.com/torognes/vsearch)
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
