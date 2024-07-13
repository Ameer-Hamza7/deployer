#!/bin/bash
docker login
cd /root/xtremeanalytix/XtremeAnalytixBridge/xtremeanalytix-data-bridge && docker compose pull && docker compose up -d 
# docker image prune -a -f
