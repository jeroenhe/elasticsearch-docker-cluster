#!/usr/bin/env bash

/wait-for-it.sh -h elasticsearch1 -p 9200 -t 180
echo "Starting CSV import for /data/blogs.csv..."

./bin/logstash -f /data/blogs_csv.conf

