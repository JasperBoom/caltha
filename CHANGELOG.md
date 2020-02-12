# Changelog

# Caltha: A python package to process UMI tagged mixed amplicon metabarcoding data.
# Copyright (C) 2018 Jasper Boom

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

## Version 0.5
+ Add code style Black.

## Version 0.4
+ Updated python script for umi5 primer single test to work with parallel processing.
+ Added zip file for umi5 primer multiple test.
+ Added parallel processing [issue #2](https://github.com/JasperBoom/caltha/issues/2).
+ Added .travis.yml configuration file.
+ Added python script for umi5 primer single test.

## Version 0.3
+ Added fasta file for umi5 primer single test.
+ Created a Zenodo DOI code for Caltha.

## Version 0.2
+ Implemented a UMI length check.
+ Created Conda package for Caltha.
+ Created PyPI package for Caltha.
+ Added documentation page to repository (still needs to be filled).
+ Zip archives are now created by Caltha (used to be created by a BASH script).
+ Temporary working directories are now managed by Caltha (used to be managed by a BASH script).
+ Wrongly assigned reads bug was fixed (PR by https://github.com/dickgroenenberg).
+ Renamed galaxy-tools-umi-isolation python tool to Caltha.
+ Isolated galaxy-tools-umi-isolation python script to dedicated repository.
