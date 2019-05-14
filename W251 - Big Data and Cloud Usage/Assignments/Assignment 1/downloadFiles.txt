#!/bin/bash
echo ${BASH_VERSION}
url='http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-2gram-20090715-'
post='.csv.zip'
for i in $(seq 0 1 32)
do
        filename='googlebooks-eng-1M-2gram-20090715-'$i'.csv'
        wget $url$i$post
done
echo completed