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

# Imports
import subprocess as sp


# The test_gzip_fasta function.
def test_gzip_fasta():
    rafRunCaltha = sp.Popen(
        [
            "./../src/caltha",
            "-i",
            "./data/umi5_primer_single.fasta.gz",
            "-t",
            "./test-output/tab.zip",
            "-z",
            "./test-output/zip.zip",
            "-b",
            "./test-output/blast.zip",
            "-f",
            "fasta",
            "-l",
            "umi5",
            "-a",
            "primer",
            "-u",
            "20",
            "-y",
            "0.97",
            "-c",
            "1",
            "-w",
            "GGRKCHGGDACWGGDTGAAC",
            "-r",
            "GATCAWACAAATAAAGGTAWTCGATC",
            "-d",
            "./test-output",
            "-@",
            "2",
        ],
        stdout=sp.PIPE,
        stderr=sp.PIPE,
    )
    strOut, strError = rafRunCaltha.communicate()
