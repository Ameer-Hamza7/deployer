#!/bin/bash
docker login
cd /root/xtremeanalytix/deployer/deployer/jobs/visualization && docker compose pull && docker compose up -d
# docker image prune -a -f
