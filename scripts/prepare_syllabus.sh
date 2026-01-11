#!/bin/bash

CURRENT_DIR=$(pwd)

cd $CURRENT_DIR

mkdir -p temp

cd temp

rm -f *.txt *.csv

cp ../egitim.ML_DL.URLs.txt .

for url in $(cat egitim.ML_DL.URLs.txt)
do
	echo $url
        echo ";;;;;" >> egitim.ML_DL.syllabus.csv
	ID=$(echo $url | cut -d'#' -f1)
	URL=$(echo $url| cut -d'#' -f2)
	ls $ID.html
	if [ ! -f $ID.html ]
	then
          curl $URL > $ID.html
	fi
	TITLE=$(grep $URL $ID.html | grep title| sed -e 's/.*title" content="//'| sed -e 's/".*//'| head -1 | sed -e 's/;/ /g'|sed -e 's/,/ /g'| sed -e 's/&amp/ and /g')
	echo $TITLE
        OLD_IFS=$IFS
	IFS=$'\n'
	for syllabus in $(grep PT[0-9]*H*[0-9]*M $ID.html | sed -e 's/Syllabus/\n/g'| grep  PT[0-9]*H*[0-9]*M | sed -e 's/\\&quot;, \\&quot;name\\&quot;: \\&quot;//'| grep -v '"'| sed -e 's/\\.*PT/ ##PT/'| sed -e 's/\\.*//g'| sed -e 's/;/ /g'|sed -e 's/,/ /g' | sed -e 's/&amp/ and /g')
	do
	     session=$(echo $syllabus| sed -e 's/##PT.*//')
	     time=$(echo $syllabus| sed -e 's/.*##PT//'| sed -e 's/M.*/M/')
	     echo "$ID;$TITLE;$URL;$session;$time;" >> egitim.ML_DL.syllabus.csv
        done
done



