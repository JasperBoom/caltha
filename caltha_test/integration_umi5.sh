#!/usr/bin/env bash

/home/jboom/caltha/src/caltha \
    -i /home/jboom/caltha/tests/data/integration.fasta \
    -t /home/jboom/caltha/caltha_test/test-output/tab.zip \
    -z /home/jboom/caltha/caltha_test/test-output/zip.zip \
    -b /home/jboom/caltha/caltha_test/test-output/blast.zip \
    -f "fasta" \
    -l "umi5" \
    -a "primer" \
    -u "8" \
    -y "0.99" \
    -c "0" \
    -w "AYACTCTCAGGWTAWAGAGC" \
    -r "GBTACCTGAAMTTTGCGGCG" \
    -d "/home/jboom/caltha/caltha_test/test-output" \
    -@ "2" \
    -e "9"
