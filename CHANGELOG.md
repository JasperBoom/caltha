# Changelog

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

## Version 0.7
+ ...

## Version 0.6
Current stable version. Previous versions should be ignored.

+ Add `pytest` file presence test function for regular fastq file input.
+ Add `pytest` file presence test function for gzipped fastq file input.
+ Add `pytest` file presence test function for regular fasta file input.
+ Re-add `pytest` test file with file presence test for gzipped fasta
  file input (further tests will be added later).
+ Remove both the umi sequence and the centroid sequence from the tabular
  output, as requested by users and noted in
  (issue 7)[https://github.com/JasperBoom/caltha/issues/7].
+ Fix fasta file creation, where new read headers would not start on a
  new line, but append to the sequence of the previous read.
+ Rename `PreZip` folders and files to `PreValidation`.
+ Fix bug where umi count would be reset to 1 for every read.
+ Replace reverse complement function with the `biopython` Seq class.
+ Add `pyfastx` for the parsing of the fasta/fastq files (which also adds
  support for single gzipped input files or multiple gzipped files in a zip
  archive).
+ Update documented python version to 3.8.
+ Rename variables in core script and update `Caltha` `--help` page.
+ Update README.md & index.md to reflect current project state.
+ Fix `pre-commit` files.

## Version 0.5.1
+ Restructure version to match PyPI package.

## Version 0.5
+ Setup `pre-commit` with `Black` and `Flake8`.

## Version 0.4
+ Add code style `Black`.

## Version 0.3
+ Updated python script for umi5 primer single test to work with parallel
  processing.
+ Added zip file for umi5 primer multiple test.

## Version 0.2
This release of `Caltha` implements parallel processing. `Caltha` now allows
a .zip file with either fasta or fastq files as input. The output has been
changed to three zip files, one for the tabular files, one for the pre
validation zip files and one for blast files.

+ Added `parallel
  processing` [issue #2](https://github.com/JasperBoom/caltha/issues/2).
+ Added `.travis.yml` configuration file.

## Version 0.1.3
+ Added python script for umi5 primer single test.

## Version 0.1.2
+ Added fasta file for umi5 primer single test.

## Version 0.1.1
+ Implemented a umi length check.

## Version 0.1
First release on GitHub for the new `Caltha` tool.
Any changes mentioned below were applied to the main python script after it was
isolated from the old "galaxy-tools-umi-isolation" repository. This python
script is now a package on PyPI and will be maintained in thism repository.

+ Created PyPI package for `Caltha`.
+ Added documentation page to repository (still needs to be filled).
+ Zip archives are now created
  by `Caltha` (used to be created by a BASH script).
+ Temporary working directories are now managed by Caltha (used to be managed
  by a BASH script).
+ Wrongly assigned reads bug was
  fixed (PR by https://github.com/dickgroenenberg).
+ Renamed `galaxy-tools-umi-isolation` python tool to `Caltha`.
+ Isolated `galaxy-tools-umi-isolation` python script to dedicated repository.
