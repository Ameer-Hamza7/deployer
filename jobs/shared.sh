#!/bin/bash
echo 'Hello world'
docker login
export DATA_BRIDGE_TAG_VERSION=version-0.0.4  
source ~/.bashrc
cd /root/xtremeanalytix/XtremeAnalytixBridge/xtremeanalytix-data-bridge && docker-compose up --force-recreate --always-recreate-deps --remove-orphans 
