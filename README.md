# Caltha
A python package to process UMI tagged mixed amplicon metabarcoding data.

## Installation
The current version of __Caltha__ requires Python 3.7+.

To install __Caltha__, simply run the pip install command:
```
pip install caltha
```

NOTE: __Caltha__ does require one more dependency which can not be installed
with pip. This dependency is [VSEARCH](https://github.com/torognes/vsearch) (2.14.1+).
Conda can be used to easily install this dependency:
```
conda install -c bioconda vsearch
```

## How to run
__Caltha__ can be run directly from the command line.
```
caltha -h

usage: caltha [-h] [-v] [-i FISINPUT] [-t FOSTABULAR] [-z FOSPREZIP]
              [-b FOSBLAST] [-f DISFORMAT] [-s DISSEARCH] [-a DISAPPROACH]
              [-u DISUMILENGTH] [-p DISIDENTITY] [-c DISABUNDANCE]
              [-w DISFORWARD] [-r DISREVERSE] [-d FISDIRECTORY]

A python package to process UMI tagged mixed amplicon metabarcoding data.

optional arguments:
  -h, --help            show this help message and exit
  -v, -version          show program's version number and exit
  -i FISINPUT, -input FISINPUT
                        The location of the input fasta/fastq file.
  -t FOSTABULAR, -tabular FOSTABULAR
                        The location of the output tabular file.
  -z FOSPREZIP, -zip FOSPREZIP
                        The location of the pre validation zip file.
  -b FOSBLAST, -blast FOSBLAST
                        The location of the output fasta file.
  -f DISFORMAT, -format DISFORMAT
                        The format of the input file [fasta/fastq].
  -s DISSEARCH, -search DISSEARCH
                        Search UMIs at the 5'-end [umi5], 3'-end [umi3] or at
                        the 5'-end and 3'-end [umidouble].
  -a DISAPPROACH, -approach DISAPPROACH
                        The UMI search approach [primer/adapter/zero].
  -u DISUMILENGTH, -length DISUMILENGTH
                        The length of the UMI sequence.
  -p DISIDENTITY, -identity DISIDENTITY
                        The identity percentage with which to perform the
                        validation.
  -c DISABUNDANCE, -abundance DISABUNDANCE
                        The minimum abundance of a read in order to be
                        included during validation.
  -w DISFORWARD, -forward DISFORWARD
                        The 5'-end search nucleotides.
  -r DISREVERSE, -reverse DISREVERSE
                        The 3'-end search nucleotides.
  -d FISDIRECTORY, -directory FISDIRECTORY
                        The location where the temporary working directory
                        will be created.

This python package requires one non-pip dependency which can be easily
installed with conda (vsearch).
```

Further documentation can be found [here](https://jasperboom.github.io/caltha/).

## Source(s)
* __Rognes T, Flouri T, Nichols B, Quince C, Mahe F__,  
  VSEARCH: a versatile open source tool for metagenomics.  
  Peerj. 2016. __doi: 10.7717/peerj.2584__  
  [VSEARCH](https://github.com/torognes/vsearch)

## Author(s)
* [Jasper Boom](https://github.com/JasperBoom)

## Citation
* __Boom J__, Caltha. 2019.  
  GitHub repository: https://github.com/JasperBoom/caltha
