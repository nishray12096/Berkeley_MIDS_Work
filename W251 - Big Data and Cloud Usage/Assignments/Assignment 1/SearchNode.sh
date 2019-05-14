#!/bin/bash

find /gpfs/gpfsfpo/mumbler -type f -name '*_node1.csv' -print0 | xargs -0 -n1 -P2 grep -e "^\<$1\>" |
gawk ' { print $2 "\t" $3 } '