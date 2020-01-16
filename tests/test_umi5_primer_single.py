#!/usr/bin/env python3
# Author: Jasper Boom

# Imports
import os
import pytest
import zipfile
import pandas as pd
import subprocess as sp
from contextlib import closing


class TestSingleEnd(object):
    def test_umi5_primer(self):
        flInput = "tests/data/umi5_primer_single.fasta"
        lstOutput = [
            "umi5_primer_single_tabular.zip",
            "umi5_primer_single_zip.zip",
            "umi5_primer_single_blast.zip",
        ]
        try:
            sp.check_output(
                [
                    "caltha",
                    "-i",
                    flInput,
                    "-t",
                    lstOutput[0],
                    "-z",
                    lstOutput[1],
                    "-b",
                    lstOutput[2],
                    "-f",
                    "fasta",
                    "-s",
                    "umi5",
                    "-a",
                    "primer",
                    "-u",
                    "20",
                    "-y",
                    "0.97",
                    "-c",
                    "2",
                    "-w",
                    "GGRKCHGGDACWGGDTGAAC",
                    "-r",
                    "GATCAWACAAATAAAGGTAWTCGATC",
                    "-d",
                    ".",
                ]
            )
        except:
            pytest.fail("umi5 primer search failed")
        lstFiles = []
        for flZip in lstOutput:
            with zipfile.ZipFile(flZip, "r") as objZip:
                lstFiles.append(zipfile.ZipFile.namelist(objZip))
                objZip.extractall(".")
        with open(lstFiles[0][0]) as oisInput:
            flTabular = pd.read_table(oisInput, sep="\t")
            intCountTabular = flTabular.shape[0]
        with closing(zipfile.ZipFile(lstFiles[1][0])) as oisInput:
            intCountZip = len(oisInput.infolist())
        with open(lstFiles[2][0]) as oisInput:
            for intCountBlast, strLine in enumerate(oisInput, 1):
                pass
        for intFile in range(len(lstOutput)):
            os.remove(lstOutput[intFile])
            for intSecondFile in range(len(lstFiles[intFile])):
                os.remove(lstFiles[intFile][intSecondFile])
        assert intCountBlast == 256, "The BLAST file should contain 256 lines."
        assert intCountZip == 658, "The zip file should contain 658 files."
        assert intCountTabular == 128, (
            "The tabular file should contain 128 "
            + "rows, excluding the header."
        )
