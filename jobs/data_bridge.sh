#!/bin/bash
echo 'login to docker ...........'
docker login
echo 'refreshing and recreatings data_bridge containers and images'
cd /root/xtremeanalytix/XtremeAnalytixBridge/xtremeanalytix-data-bridge && docker-compose pull && docker-compose up -d --force-recreate --always-recreate-deps
echo 'cleaning all unsed images .........'
docker image prune -a -f
