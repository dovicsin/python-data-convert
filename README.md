# Python data convert script example

Data convert from agregated log line to xlsx with Python

## The blog post:

* [Adat átalakítás folytonos szövegből Excel táblázatba](https://oa.webspecial.hu/posts/python-adat-atalakitas-folytonos-szoevegbol-excel-tablazatba/)


## The example agregate bash script (the date of month replace Hungarian short names): 

cat linkList.txt | while read line; do echo $line;  grep -E -i "GET $line/?(index.html)?([\?#].*)? HTTP/1.1" /var/log/access_log* | grep -vE '.*\.(bot|svg|SVG|css|js|png|jpg|jpeg|gif|PNG|JPG|JPEG|GIF)|404|206|User-Agent:.*bot|bot|robot|192\.168\.(?!(227\.(25[12]|31))).*$'| awk 'match($0,/\[[0-9]{2}\/[A-Z][a-z]{2}\/[0-9]{4}:([0-9]{2}:?){3}\s\+[0-9]*\]/) { print substr($0,RSTART+4,RLENGTH-20)}' | awk '{split($0, array, "/"); printf $0 = array[2]"/%02d\n",index("  JanFebMarAprMayJunJulAugSepOctNovDec", array[1])/3 '} | sort  | uniq -c; done > result.txt

This command read every line in txt and find the access log with grep. After filter the other file url, local ip and robot. And before convert and short the new structure with awk.
