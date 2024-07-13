#!/bin/bash
docker login
cd /root/xtremeanalytix/XtremeAnalytixBridge/xtremeanalytix-data-bridge && dockercompose pull && dockercompose up -d
# docker image prune -a -f
