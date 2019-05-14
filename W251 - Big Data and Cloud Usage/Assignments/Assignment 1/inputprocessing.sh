#!/bin/bash
loopstart=$1

loopend=$2
echo 'Processing files '$loopstart' To '$loopend
for i in $(seq $loopstart 1 $loopend)
do
        echo 'Processing '$i
        filename='googlebooks-eng-all-2gram-20090715-'$i'.csv'
        procname='googlebooks-eng-all-2gram-20090715-'$i'proc.csv'

    unzip -p $filename'.zip' |
        awk '
        BEGIN {ng1 = ""; ng2 = ""; matches=0; }
        {
          if( NF == 6) {
          if( ng1 != $1 || ng2 != $2)
          {
            if( matches > 0) print ng1 "\t" ng2 "\t" matches;
            ng1 = $1;
            ng2 = $2;
            matches = $4;
          }
          else matches += $4;
        }
      }
      END { if( matches > 0) print ng1 "\t" ng2 "\t" matches;}' > $procname
        rm $filename'.zip'
done