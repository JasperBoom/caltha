#!/usr/bin/env python3

# Author: Jasper Boom

# Prequisites:
# - conda install -c bioconda vsearch=2.14.1

# Imports
import os
import pytest
import zipfile
import pandas as pd
import subprocess as sp
from contextlib import closing

class TestSingleEnd(object):
    def test_umi5_primer(self):
        flInput = "data/umi5_primer.fasta"
        lstOutput = ["tabular.tbl", "zip.zip", "blast.fasta"]
        try:
            sp.check_output(
                ["caltha", "-i", flInput,
                 "-t", lstOutput[0],
                 "-z", lstOutput[1],
                 "-b", lstOutput[2],
                 "-f", "fasta",
                 "-s", "umi5",
                 "-a", "primer",
                 "-u", "20",
                 "-p", "0.97",
                 "-c", "2",
                 "-w", "GGRKCHGGDACWGGDTGAAC",
                 "-r", "GATCAWACAAATAAAGGTAWTCGATC",
                 "-d", "."])
        except:
            pytest.fail("umi5 primer search failed")
        with open("blast.fasta") as oisInput:
            for intCountBlast, strLine in enumerate(oisInput, 1):
                pass
        with closing(zipfile.ZipFile("zip.zip")) as oisInput:
            intCountZip = len(oisInput.infolist())
        with open("tabular.tbl") as oisInput:
            flTabular = pd.read_table(oisInput, sep="\t")
            intCountTabular = flTabular.shape[0]
        for intFile in range(len(lstOutput)):
            os.remove(lstOutput[intFile])
        assert intCountBlast == 256, "The BLAST file should contain 256 lines."
        assert intCountZip == 658, "The zip file should contain 658 files."
        assert intCountTabular == 128, "The tabular file should contain 128 " +\
                                       "rows, excluding the header."