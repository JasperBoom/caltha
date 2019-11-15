## How to run
__Caltha__ can be run directly from the command line.
```
caltha -h

usage: caltha [-h] [-v] [-i FISINPUT] [-t FOSTABULAR] [-z FOSPREZIP]
              [-b FOSBLAST] [-f DISFORMAT] [-s DISSEARCH] [-a DISAPPROACH]
              [-u DISUMILENGTH] [-y DISIDENTITY] [-c DISABUNDANCE]
              [-w DISFORWARD] [-r DISREVERSE] [-d FISDIRECTORY]
              [-p DISPROCESSES]

A python package to process UMI tagged mixed amplicon metabarcoding data.

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
                        Search UMIs at the 5'-end [umi5], 3'-end [umi3] or at
                        the 5'-end and 3'-end [umidouble]. (default: umi5)
  -a DISAPPROACH, -approach DISAPPROACH
                        The UMI search approach [primer/adapter/zero].
                        (default: primer)
  -u DISUMILENGTH, -length DISUMILENGTH
                        The length of the UMI sequence.
  -y DISIDENTITY, -identity DISIDENTITY
                        The identity percentage with which to perform the
                        validation. (default: 0.97)
  -c DISABUNDANCE, -abundance DISABUNDANCE
                        The minimum abundance of a read in order to be
                        included during validation. (default: 1)
  -w DISFORWARD, -forward DISFORWARD
                        The 5'-end search nucleotides.
  -r DISREVERSE, -reverse DISREVERSE
                        The 3'-end search nucleotides.
  -d FISDIRECTORY, -directory FISDIRECTORY
                        The location where the temporary working directory
                        will be created. (default: .)
  -p DISPROCESSES, -processes DISPROCESSES
                        The number of threads/cores/processes to
                        simultaneously run Caltha with. (default: number of cores available)

This python package requires one extra dependency which can be easily
installed with conda (conda install -c bioconda vsearch).
```

## Package links
* [PyPI](https://pypi.org/project/caltha/)
* [Conda](https://anaconda.org/jboom/caltha)

## Source(s)
* __Giardine B, Riemer C, Hardison RC, Burhans R, Elnitski L, Shah P__,  
  Galaxy: A platform for interactive large-scale genome analysis.  
  Genome Research. 2005; 15(10) 1451-1455 __doi: 10.1101/gr.4086505__  
  [GALAXY](https://www.galaxyproject.org/)
* __Python Software Foundation__,  
  Python 3.7+, 2019.  
  [Python](https://www.python.org/)
* __Rognes T, Flouri T, Nichols B, Quince C, Mahe F__,
  VSEARCH: A versatile open source tool for metagenomics.  
  PeerJ. 2016; __doi: 10.7717/peerj.2584__  
  [VSEARCH](https://github.com/torognes/vsearch)
* __Augspurger T, Ayd W, Bartak C, Battiston P, Cloud P, Garcia M__,  
  Python Data Analysis Library.  
  [Pandas](https://pandas.pydata.org/)

## Author(s)
* [Jasper Boom](https://github.com/JasperBoom)

## Citation
* __Boom J__, Caltha. 2019.  
  [![DOI](https://zenodo.org/badge/216898964.svg)](https://zenodo.org/badge/latestdoi/216898964)  
  GitHub repository: https://github.com/JasperBoom/caltha
