#!/bin/bash
#enter input encoding here
FROM_ENCODING="macintosh"
#output encoding(UTF-8)
TO_ENCODING="utf-8"
#convert
CONVERT=" iconv  -f   $FROM_ENCODING  -t   $TO_ENCODING"
#loop to convert multiple files
for  file  in  Umsatz*.csv; do
    if [[ ${file} != *"converted"* ]];then
        $CONVERT   "$file"   >  "${file%.csv}_utf8_converted.csv"
    fi
done
exit 0