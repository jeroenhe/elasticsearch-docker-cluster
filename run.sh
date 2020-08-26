#!/usr/bin/env bash

docker-compose --compatibility up -d --build && docker-compose --compatibility logs -f
