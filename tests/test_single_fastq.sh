#!/usr/bin/env bash

/home/jboom/Temp/caltha/src/caltha \
    -i /home/jboom/Temp/caltha/tests/data/umi5_primer_single.fastq \
    -t /home/jboom/Temp/test-output/tab.zip \
    -z /home/jboom/Temp/test-output/zip.zip \
    -b /home/jboom/Temp/test-output/blast.zip \
    -f "fastq" \
    -l "umi5" \
    -a "primer" \
    -u "20" \
    -y "0.97" \
    -c "1" \
    -w "GGRKCHGGDACWGGDTGAAC" \
    -r "GATCAWACAAATAAAGGTAWTCGATC" \
    -d "/home/jboom/Temp/test-output" \
    -@ "2"
