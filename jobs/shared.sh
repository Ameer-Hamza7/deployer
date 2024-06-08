#!/bin/bash
echo 'Hello world'
docker login
$DATA_BRIDGE_TAG_VERSION=version-0.0.4  
cd /root/xtremeanalytix/XtremeAnalytixBridge/xtremeanalytix-data-bridge && docker-cmpose up --force-recreate --always-recreate-deps --remove-orphans 