#!/usr/bin/env bash

/wait-for-it.sh -h elasticsearch1 -p 9200 -t 180
echo "Starting logs import for /data/elastic*..."

./filebeat -c /data/filebeat.yml
