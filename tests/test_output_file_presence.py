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


# The test_fasta function.
def rtest_fasta():
    strOutputDirectory = "/home/travis/build/JasperBoom/test-output/fasta"
    strTestDirectory = "/home/travis/build/JasperBoom/caltha/tests"
    os.makedirs(strOutputDirectory)
    sp.call(
        [
            "/home/travis/build/JasperBoom/caltha/src/caltha",
            "-i",
            strTestDirectory + "/data/umi5_primer_single.fasta",
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
            "1",
        ],
    )

    with zipfile.ZipFile(strOutputDirectory + "/blast.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)
    with zipfile.ZipFile(strOutputDirectory + "/tab.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)
    with zipfile.ZipFile(strOutputDirectory + "/zip.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)

    lstOutputFiles = [
        "umi5_primer_single_BLAST.fasta",
        "umi5_primer_single_TABULAR.tbl",
    ]
    dicLineCounts = {}

    for strFileName in lstOutputFiles:
        with open(strOutputDirectory + "/" + strFileName) as oisBlastFile:
            intLineCount = 0
            for strLine in oisBlastFile:
                intLineCount += 1
        dicLineCounts[strFileName] = intLineCount

    lstOutputZips = ["umi5_primer_single_PREVALIDATION.zip"]

    for strZipFile in lstOutputZips:
        if (
            os.path.exists(strOutputDirectory + "/" + strZipFile)
            and os.path.getsize(strOutputDirectory + "/" + strZipFile) > 0
        ):
            blnArchiveCheck = 1
        else:
            blnArchiveCheck = 0
        assert blnArchiveCheck == 1

    assert dicLineCounts["umi5_primer_single_BLAST.fasta"] == 1560
    assert dicLineCounts["umi5_primer_single_TABULAR.tbl"] == 781


# The test_gzip_fasta function.
def rtest_gzip_fasta():
    strOutputDirectory = "/home/travis/build/JasperBoom/test-output/gzip-fasta"
    strTestDirectory = "/home/travis/build/JasperBoom/caltha/tests"
    os.makedirs(strOutputDirectory)
    sp.call(
        [
            "/home/travis/build/JasperBoom/caltha/src/caltha",
            "-i",
            strTestDirectory + "/data/umi5_primer_gzip.fasta.gz",
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
            "1",
        ],
    )

    with zipfile.ZipFile(strOutputDirectory + "/blast.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)
    with zipfile.ZipFile(strOutputDirectory + "/tab.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)
    with zipfile.ZipFile(strOutputDirectory + "/zip.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)

    lstOutputFiles = [
        "umi5_primer_gzip_BLAST.fasta",
        "umi5_primer_gzip_TABULAR.tbl",
    ]
    dicLineCounts = {}

    for strFileName in lstOutputFiles:
        with open(strOutputDirectory + "/" + strFileName) as oisBlastFile:
            intLineCount = 0
            for strLine in oisBlastFile:
                intLineCount += 1
        dicLineCounts[strFileName] = intLineCount

    lstOutputZips = ["umi5_primer_gzip_PREVALIDATION.zip"]

    for strZipFile in lstOutputZips:
        if (
            os.path.exists(strOutputDirectory + "/" + strZipFile)
            and os.path.getsize(strOutputDirectory + "/" + strZipFile) > 0
        ):
            blnArchiveCheck = 1
        else:
            blnArchiveCheck = 0
        assert blnArchiveCheck == 1

    assert dicLineCounts["umi5_primer_gzip_BLAST.fasta"] == 1560
    assert dicLineCounts["umi5_primer_gzip_TABULAR.tbl"] == 781


# The test_fastq function.
def test_fastq():
    strOutputDirectory = "/home/travis/build/JasperBoom/test-output/fastq"
    strTestDirectory = "/home/travis/build/JasperBoom/caltha/tests"
    os.makedirs(strOutputDirectory)
    sp.call(
        [
            "/home/travis/build/JasperBoom/caltha/src/caltha",
            "-i",
            strTestDirectory + "/data/umi5_primer_single.fastq",
            "-t",
            strOutputDirectory + "/tab.zip",
            "-z",
            strOutputDirectory + "/zip.zip",
            "-b",
            strOutputDirectory + "/blast.zip",
            "-f",
            "fastq",
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
            "1",
        ],
    )

    with zipfile.ZipFile(strOutputDirectory + "/blast.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)
    with zipfile.ZipFile(strOutputDirectory + "/tab.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)
    with zipfile.ZipFile(strOutputDirectory + "/zip.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)

    lstOutputFiles = [
        "umi5_primer_single_BLAST.fasta",
        "umi5_primer_single_TABULAR.tbl",
    ]
    dicLineCounts = {}

    for strFileName in lstOutputFiles:
        with open(strOutputDirectory + "/" + strFileName) as oisBlastFile:
            intLineCount = 0
            for strLine in oisBlastFile:
                intLineCount += 1
        dicLineCounts[strFileName] = intLineCount

    lstOutputZips = ["umi5_primer_single_PREVALIDATION.zip"]

    for strZipFile in lstOutputZips:
        if (
            os.path.exists(strOutputDirectory + "/" + strZipFile)
            and os.path.getsize(strOutputDirectory + "/" + strZipFile) > 0
        ):
            blnArchiveCheck = 1
        else:
            blnArchiveCheck = 0
        assert blnArchiveCheck == 1

    assert dicLineCounts["umi5_primer_single_BLAST.fasta"] == 1560
    assert dicLineCounts["umi5_primer_single_TABULAR.tbl"] == 781


# The test_gzip_fastq function.
def test_gzip_fastq():
    strOutputDirectory = "/home/travis/build/JasperBoom/test-output/gzip-fastq"
    strTestDirectory = "/home/travis/build/JasperBoom/caltha/tests"
    os.makedirs(strOutputDirectory)
    sp.call(
        [
            "/home/travis/build/JasperBoom/caltha/src/caltha",
            "-i",
            strTestDirectory + "/data/umi5_primer_gzip.fastq.gz",
            "-t",
            strOutputDirectory + "/tab.zip",
            "-z",
            strOutputDirectory + "/zip.zip",
            "-b",
            strOutputDirectory + "/blast.zip",
            "-f",
            "fastq",
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
            "1",
        ],
    )

    with zipfile.ZipFile(strOutputDirectory + "/blast.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)
    with zipfile.ZipFile(strOutputDirectory + "/tab.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)
    with zipfile.ZipFile(strOutputDirectory + "/zip.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)

    lstOutputFiles = [
        "umi5_primer_gzip_BLAST.fasta",
        "umi5_primer_gzip_TABULAR.tbl",
    ]
    dicLineCounts = {}

    for strFileName in lstOutputFiles:
        with open(strOutputDirectory + "/" + strFileName) as oisBlastFile:
            intLineCount = 0
            for strLine in oisBlastFile:
                intLineCount += 1
        dicLineCounts[strFileName] = intLineCount

    lstOutputZips = ["umi5_primer_gzip_PREVALIDATION.zip"]

    for strZipFile in lstOutputZips:
        if (
            os.path.exists(strOutputDirectory + "/" + strZipFile)
            and os.path.getsize(strOutputDirectory + "/" + strZipFile) > 0
        ):
            blnArchiveCheck = 1
        else:
            blnArchiveCheck = 0
        assert blnArchiveCheck == 1

    assert dicLineCounts["umi5_primer_gzip_BLAST.fasta"] == 1560
    assert dicLineCounts["umi5_primer_gzip_TABULAR.tbl"] == 781


# The test_multiple_fasta_zip function.
def rtest_multiple_fasta_zip():
    strOutputDirectory = (
        "/home/travis/build/JasperBoom/test-output/multiple_fasta_zip"
    )
    strTestDirectory = "/home/travis/build/JasperBoom/caltha/tests"
    os.makedirs(strOutputDirectory)
    sp.call(
        [
            "/home/travis/build/JasperBoom/caltha/src/caltha",
            "-i",
            strTestDirectory + "/data/umi5_primer_multiple.zip",
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
            "3",
        ],
    )

    with zipfile.ZipFile(strOutputDirectory + "/blast.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)
    with zipfile.ZipFile(strOutputDirectory + "/tab.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)
    with zipfile.ZipFile(strOutputDirectory + "/zip.zip", "r") as objZip:
        objZip.extractall(strOutputDirectory)

    lstOutputFiles = [
        "zipTest1_BLAST.fasta",
        "zipTest1_TABULAR.tbl",
        "zipTest2_BLAST.fasta",
        "zipTest2_TABULAR.tbl",
        "zipTest3_BLAST.fasta",
        "zipTest3_TABULAR.tbl",
    ]
    dicLineCounts = {}

    for strFileName in lstOutputFiles:
        with open(strOutputDirectory + "/" + strFileName) as oisBlastFile:
            intLineCount = 0
            for strLine in oisBlastFile:
                intLineCount += 1
        dicLineCounts[strFileName] = intLineCount

    lstOutputZips = [
        "zipTest1_PREVALIDATION.zip",
        "zipTest2_PREVALIDATION.zip",
        "zipTest3_PREVALIDATION.zip",
    ]

    for strZipFile in lstOutputZips:
        if (
            os.path.exists(strOutputDirectory + "/" + strZipFile)
            and os.path.getsize(strOutputDirectory + "/" + strZipFile) > 0
        ):
            blnArchiveCheck = 1
        else:
            blnArchiveCheck = 0
        assert blnArchiveCheck == 1

    assert dicLineCounts["zipTest1_BLAST.fasta"] == 1560
    assert dicLineCounts["zipTest1_TABULAR.tbl"] == 781
    assert dicLineCounts["zipTest2_BLAST.fasta"] == 1560
    assert dicLineCounts["zipTest2_TABULAR.tbl"] == 781
    assert dicLineCounts["zipTest3_BLAST.fasta"] == 1560
    assert dicLineCounts["zipTest3_TABULAR.tbl"] == 781
