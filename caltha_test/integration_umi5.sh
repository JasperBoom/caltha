#!/usr/bin/env bash

/mnt/e/ubuntu/caltha/src/caltha \
    -i /mnt/e/ubuntu/caltha/tests/data/integration.fasta \
    -t /mnt/e/ubuntu/test-output/tab.zip \
    -z /mnt/e/ubuntu/test-output/zip.zip \
    -b /mnt/e/ubuntu/test-output/blast.zip \
    -f "fasta" \
    -l "umi5" \
    -a "primer" \
    -u "8" \
    -y "0.99" \
    -c "0" \
    -w "AYACTCTCAGGWTAWAGAGC" \
    -r "GBTACCTGAAMTTTGCGGCG" \
    -d "/mnt/e/ubuntu/test-output" \
    -@ "2"
