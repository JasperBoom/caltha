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
import os
import zipfile
import subprocess as sp


# The test_gzip_fasta function.
def test_gzip_fasta():
    strOutputDirectory = "/home/travis/build/JasperBoom/test-output"
    os.mkdir(strOutputDirectory)
    rafRunCaltha = sp.Popen(
        [
            "/home/travis/build/JasperBoom/caltha/src/caltha",
            "-i",
            "/home/travis/build/JasperBoom/caltha/tests/data/\
             umi5_primer_single.fasta.gz",
            "-t",
            "/home/travis/build/JasperBoom/caltha/tests/test-output/tab.zip",
            "-z",
            "/home/travis/build/JasperBoom/caltha/tests/test-output/zip.zip",
            "-b",
            "/home/travis/build/JasperBoom/caltha/tests/test-output/blast.zip",
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
            strOutputDirectory,
            "-@",
            "2",
        ],
        stdout=sp.PIPE,
        stderr=sp.PIPE,
    )
    strOut, strError = rafRunCaltha.communicate()

    with zipfile.ZipFile(strOutputDirectory + "/blast.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)

    with open(
        strOutputDirectory + "umi5_primer_single_BLAST.fasta"
    ) as oisBlastFile:
        intBlastLineCount = 0
        for strLine in oisBlastFile:
            intBlastLineCount += 1

    assert intBlastLineCount == 1560
