#!/bin/bash

# Directory where CSV files are located
dir='./data'

# Name of the output file
outputFile='combined.csv'

# Remove the output file if it exists
rm -f $outputFile

# Process the CSV files
for file in $(ls $dir/Metadata_Country_API*.csv)
do
    echo $file
    awk -F '",' '
    BEGIN {OFS = FS} 
    NR>1 {
        if ($1 ~ /Country Code/ && $4 ~ /SpecialNotes/) {
            print $1, $2, $3, $4, $5 >> "'$outputFile'"
        } 
        else if ($1 ~ /Country Code/ && $4 ~ /TableName/) {
            print $1, $2, $3, $5, $4 >> "'$outputFile'"
        }
    }' "$file"
done
