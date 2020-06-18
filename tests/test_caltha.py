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
    strTestDirectory = "/home/travis/build/JasperBoom/caltha/tests"
    os.mkdir(strOutputDirectory)
    sp.call(
        [
            "/home/travis/build/JasperBoom/caltha/src/caltha",
            "-i",
            strTestDirectory + "/data/umi5_primer_single.fasta.gz",
            "-t",
            strOutputDirectory + "/tab.zip",
            "-z",
            strOutputDirectory + "/zip.zip",
            "-b",
            strOutputDirectory + "/blast.zip",
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
    )

    with zipfile.ZipFile(strOutputDirectory + "/blast.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)
    with zipfile.ZipFile(strOutputDirectory + "/tab.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)
    with zipfile.ZipFile(strOutputDirectory + "/zip.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)

    with open(
        strOutputDirectory + "/umi5_primer_single_BLAST.fasta"
    ) as oisBlastFile:
        intBlastLineCount = 0
        for strLine in oisBlastFile:
            intBlastLineCount += 1

    with open(
        strOutputDirectory + "/umi5_primer_single_TABULAR.tbl"
    ) as oisBlastFile:
        intTabularLineCount = 0
        for strLine in oisBlastFile:
            intTabularLineCount += 1

    if (
        os.path.exists(
            strOutputDirectory + "/umi5_primer_single_PREVALIDATION.zip"
        )
        and os.path.getsize(
            strOutputDirectory + "/umi5_primer_single_PREVALIDATION.zip"
        )
        > 0
    ):
        blnArchiveCheck = True
    else:
        blnArchiveCheck = False

    assert intBlastLineCount == 1560
    assert intTabularLineCount == 781
    assert blnArchiveCheck
