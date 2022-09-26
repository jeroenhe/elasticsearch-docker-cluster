#!/usr/bin/env bash

/wait-for-it.sh -h elasticsearch1 -p 9200 -t 180

echo "Verify index does not yet exist, so we import it only once..."

curl -sSf "http://elasticsearch1:9200/logs_server1/_count"
EXIT_CODE=$?

echo "Curl exited with '${EXIT_CODE}'"

if [ "${EXIT_CODE}" != "0" ]; then
    echo "Starting log files import for /data/elastic*..."
    ./filebeat -c /data/filebeat.yml
    echo "Import finished."
else
    echo "Indices logs_server* where already imported. Skipping."
fi

exit 0
