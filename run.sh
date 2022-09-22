#!/usr/bin/env bash

# When you exit this script via crtl-c, the contains keep continue running in the background
docker compose up -d --build && \
    docker compose logs -f
