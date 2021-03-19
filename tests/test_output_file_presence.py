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

"""
Imports:
"""
import os
import zipfile
import subprocess as sp


def test_fasta():
    """
    The test_fasta function:
    """
    output_directory = "/home/travis/build/JasperBoom/test-output/fasta"
    test_directory = "/home/travis/build/JasperBoom/caltha/tests"
    os.makedirs(output_directory)
    sp.call(
        [
            "/home/travis/build/JasperBoom/caltha/src/caltha",
            "-i",
            test_directory + "/data/umi5_primer_single.fasta",
            "-t",
            output_directory + "/tab.zip",
            "-z",
            output_directory + "/zip.zip",
            "-b",
            output_directory + "/blast.zip",
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
            output_directory,
            "-@",
            "1",
        ],
    )

    with zipfile.ZipFile(output_directory + "/blast.zip", "r") as zip_object:
        zip_object.extractall(output_directory)
    with zipfile.ZipFile(output_directory + "/tab.zip", "r") as zip_object:
        zip_object.extractall(output_directory)
    with zipfile.ZipFile(output_directory + "/zip.zip", "r") as zip_object:
        zip_object.extractall(output_directory)

    output_files_list = [
        "umi5_primer_single_BLAST.fasta",
        "umi5_primer_single_TABULAR.tbl",
    ]
    line_counts_dictionary = {}

    for file_name in output_files_list:
        with open(output_directory + "/" + file_name) as blast_file:
            line_count = 0
            for line in blast_file:
                line_count += 1
        line_counts_dictionary[file_name] = line_count

    output_zip_files = ["umi5_primer_single_PREVALIDATION.zip"]

    for zip_file in output_zip_files:
        if (
            os.path.exists(output_directory + "/" + zip_file)
            and os.path.getsize(output_directory + "/" + zip_file) > 0
        ):
            zip_archive_check = 1
        else:
            zip_archive_check = 0
        assert zip_archive_check == 1

    assert line_counts_dictionary["umi5_primer_single_BLAST.fasta"] == 1560
    assert line_counts_dictionary["umi5_primer_single_TABULAR.tbl"] == 781


def test_gzip_fasta():
    """
    The test_gzip_fasta function:
    """
    output_directory = "/home/travis/build/JasperBoom/test-output/gzip-fasta"
    test_directory = "/home/travis/build/JasperBoom/caltha/tests"
    os.makedirs(output_directory)
    sp.call(
        [
            "/home/travis/build/JasperBoom/caltha/src/caltha",
            "-i",
            test_directory + "/data/umi5_primer_gzip.fasta.gz",
            "-t",
            output_directory + "/tab.zip",
            "-z",
            output_directory + "/zip.zip",
            "-b",
            output_directory + "/blast.zip",
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
            output_directory,
            "-@",
            "1",
        ],
    )

    with zipfile.ZipFile(output_directory + "/blast.zip", "r") as zip_object:
        zip_object.extractall(output_directory)
    with zipfile.ZipFile(output_directory + "/tab.zip", "r") as zip_object:
        zip_object.extractall(output_directory)
    with zipfile.ZipFile(output_directory + "/zip.zip", "r") as zip_object:
        zip_object.extractall(output_directory)

    output_files_list = [
        "umi5_primer_gzip_BLAST.fasta",
        "umi5_primer_gzip_TABULAR.tbl",
    ]
    line_counts_dictionary = {}

    for file_name in output_files_list:
        with open(output_directory + "/" + file_name) as blast_file:
            line_count = 0
            for line in blast_file:
                line_count += 1
        line_counts_dictionary[file_name] = line_count

    output_zip_files = ["umi5_primer_gzip_PREVALIDATION.zip"]

    for zip_file in output_zip_files:
        if (
            os.path.exists(output_directory + "/" + zip_file)
            and os.path.getsize(output_directory + "/" + zip_file) > 0
        ):
            zip_archive_check = 1
        else:
            zip_archive_check = 0
        assert zip_archive_check == 1

    assert line_counts_dictionary["umi5_primer_gzip_BLAST.fasta"] == 1560
    assert line_counts_dictionary["umi5_primer_gzip_TABULAR.tbl"] == 781


def test_fastq():
    """
    The test_fastq function:
    """
    output_directory = "/home/travis/build/JasperBoom/test-output/fastq"
    test_directory = "/home/travis/build/JasperBoom/caltha/tests"
    os.makedirs(output_directory)
    sp.call(
        [
            "/home/travis/build/JasperBoom/caltha/src/caltha",
            "-i",
            test_directory + "/data/umi5_primer_single.fastq",
            "-t",
            output_directory + "/tab.zip",
            "-z",
            output_directory + "/zip.zip",
            "-b",
            output_directory + "/blast.zip",
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
            output_directory,
            "-@",
            "1",
        ],
    )

    with zipfile.ZipFile(output_directory + "/blast.zip", "r") as zip_object:
        zip_object.extractall(output_directory)
    with zipfile.ZipFile(output_directory + "/tab.zip", "r") as zip_object:
        zip_object.extractall(output_directory)
    with zipfile.ZipFile(output_directory + "/zip.zip", "r") as zip_object:
        zip_object.extractall(output_directory)

    output_files_list = [
        "umi5_primer_single_BLAST.fasta",
        "umi5_primer_single_TABULAR.tbl",
    ]
    line_counts_dictionary = {}

    for file_name in output_files_list:
        with open(output_directory + "/" + file_name) as blast_file:
            line_count = 0
            for line in blast_file:
                line_count += 1
        line_counts_dictionary[file_name] = line_count

    output_zip_files = ["umi5_primer_single_PREVALIDATION.zip"]

    for zip_file in output_zip_files:
        if (
            os.path.exists(output_directory + "/" + zip_file)
            and os.path.getsize(output_directory + "/" + zip_file) > 0
        ):
            zip_archive_check = 1
        else:
            zip_archive_check = 0
        assert zip_archive_check == 1

    assert line_counts_dictionary["umi5_primer_single_BLAST.fasta"] == 1560
    assert line_counts_dictionary["umi5_primer_single_TABULAR.tbl"] == 781


def test_gzip_fastq():
    """
    The test_gzip_fastq function:
    """
    output_directory = "/home/travis/build/JasperBoom/test-output/gzip-fastq"
    test_directory = "/home/travis/build/JasperBoom/caltha/tests"
    os.makedirs(output_directory)
    sp.call(
        [
            "/home/travis/build/JasperBoom/caltha/src/caltha",
            "-i",
            test_directory + "/data/umi5_primer_gzip.fastq.gz",
            "-t",
            output_directory + "/tab.zip",
            "-z",
            output_directory + "/zip.zip",
            "-b",
            output_directory + "/blast.zip",
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
            output_directory,
            "-@",
            "1",
        ],
    )

    with zipfile.ZipFile(output_directory + "/blast.zip", "r") as zip_object:
        zip_object.extractall(output_directory)
    with zipfile.ZipFile(output_directory + "/tab.zip", "r") as zip_object:
        zip_object.extractall(output_directory)
    with zipfile.ZipFile(output_directory + "/zip.zip", "r") as zip_object:
        zip_object.extractall(output_directory)

    output_files_list = [
        "umi5_primer_gzip_BLAST.fasta",
        "umi5_primer_gzip_TABULAR.tbl",
    ]
    line_counts_dictionary = {}

    for file_name in output_files_list:
        with open(output_directory + "/" + file_name) as blast_file:
            line_count = 0
            for line in blast_file:
                line_count += 1
        line_counts_dictionary[file_name] = line_count

    output_zip_files = ["umi5_primer_gzip_PREVALIDATION.zip"]

    for zip_file in output_zip_files:
        if (
            os.path.exists(output_directory + "/" + zip_file)
            and os.path.getsize(output_directory + "/" + zip_file) > 0
        ):
            zip_archive_check = 1
        else:
            zip_archive_check = 0
        assert zip_archive_check == 1

    assert line_counts_dictionary["umi5_primer_gzip_BLAST.fasta"] == 1560
    assert line_counts_dictionary["umi5_primer_gzip_TABULAR.tbl"] == 781


def test_multiple_fasta_zip():
    """
    The test_multiple_fasta_zip function:
    """
    output_directory = (
        "/home/travis/build/JasperBoom/test-output/multiple_fasta_zip"
    )
    test_directory = "/home/travis/build/JasperBoom/caltha/tests"
    os.makedirs(output_directory)
    sp.call(
        [
            "/home/travis/build/JasperBoom/caltha/src/caltha",
            "-i",
            test_directory + "/data/umi5_primer_multiple.zip",
            "-t",
            output_directory + "/tab.zip",
            "-z",
            output_directory + "/zip.zip",
            "-b",
            output_directory + "/blast.zip",
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
            output_directory,
            "-@",
            "3",
        ],
    )

    with zipfile.ZipFile(output_directory + "/blast.zip", "r") as zip_object:
        zip_object.extractall(output_directory)
    with zipfile.ZipFile(output_directory + "/tab.zip", "r") as zip_object:
        zip_object.extractall(output_directory)
    with zipfile.ZipFile(output_directory + "/zip.zip", "r") as zip_object:
        zip_object.extractall(output_directory)

    output_files_list = [
        "zipTest1_BLAST.fasta",
        "zipTest1_TABULAR.tbl",
        "zipTest2_BLAST.fasta",
        "zipTest2_TABULAR.tbl",
        "zipTest3_BLAST.fasta",
        "zipTest3_TABULAR.tbl",
    ]
    line_counts_dictionary = {}

    for file_name in output_files_list:
        with open(output_directory + "/" + file_name) as blast_file:
            line_count = 0
            for line in blast_file:
                line_count += 1
        line_counts_dictionary[file_name] = line_count

    output_zip_files = [
        "zipTest1_PREVALIDATION.zip",
        "zipTest2_PREVALIDATION.zip",
        "zipTest3_PREVALIDATION.zip",
    ]

    for zip_file in output_zip_files:
        if (
            os.path.exists(output_directory + "/" + zip_file)
            and os.path.getsize(output_directory + "/" + zip_file) > 0
        ):
            zip_archive_check = 1
        else:
            zip_archive_check = 0
        assert zip_archive_check == 1

    assert line_counts_dictionary["zipTest1_BLAST.fasta"] == 1560
    assert line_counts_dictionary["zipTest1_TABULAR.tbl"] == 781
    assert line_counts_dictionary["zipTest2_BLAST.fasta"] == 1560
    assert line_counts_dictionary["zipTest2_TABULAR.tbl"] == 781
    assert line_counts_dictionary["zipTest3_BLAST.fasta"] == 1560
    assert line_counts_dictionary["zipTest3_TABULAR.tbl"] == 781

"""
Additional information:
"""
