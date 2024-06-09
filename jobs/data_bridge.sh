#!/bin/bash
docker login  
cd /root/xtremeanalytix/XtremeAnalytixBridge/xtremeanalytix-data-bridge && docker-cmpose up --force-recreate --always-recreate-deps --remove-orphans
docker image prune
