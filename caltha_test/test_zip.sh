#!/usr/bin/env bash

/home/jboom/Temp/caltha/src/caltha \
    -i /home/jboom/Temp/caltha/tests/data/umi5_primer_multiple.zip \
    -t /home/jboom/Temp/test-output/tab.zip \
    -z /home/jboom/Temp/test-output/zip.zip \
    -b /home/jboom/Temp/test-output/blast.zip \
    -f "fasta" \
    -l "umi5" \
    -a "primer" \
    -u "20" \
    -y "0.97" \
    -c "1" \
    -w "GGRKCHGGDACWGGDTGAAC" \
    -r "GATCAWACAAATAAAGGTAWTCGATC" \
    -d "/home/jboom/Temp/caltha_test/test-output" \
    -@ "2"