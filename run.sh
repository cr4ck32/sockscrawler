rm *.csv
scrapy runspider main.py -o data.csv -t csv
awk  '{FS=","; OFS="\t"; print $3,$1,$2}'< data.csv > proxy.csv
sed -i 's/Socks/socks/g' proxy.csv
