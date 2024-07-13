#!/bin/bash
docker login
cd /root/xtremeanalytix/deployer/deployer/jobs/visualization && dockercompose down && dockercompose pull && dockercompose up -d
# docker image prune -a -f
