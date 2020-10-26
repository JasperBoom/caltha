#!/usr/bin/env bash

/mnt/e/ubuntu/caltha/src/caltha \
    -i /mnt/e/ubuntu/caltha/tests/data/mock.community.reads.fasta \
    -t /mnt/e/ubuntu/test-output/tab.zip \
    -z /mnt/e/ubuntu/test-output/zip.zip \
    -b /mnt/e/ubuntu/test-output/blast.zip \
    -f "fasta" \
    -l "umi3" \
    -a "primer" \
    -u "8" \
    -y "0.99" \
    -c "1" \
    -w "AYACTCTCAGGWTAWAGAGC" \
    -r "GBTACCTGAAMTTTGCGGCG" \
    -d "/mnt/e/ubuntu/test-output" \
    -@ "2"
