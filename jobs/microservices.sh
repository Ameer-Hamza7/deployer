#!/bin/bash
docker login
cd /root/xtremeanalytix/deployer/deployer/jobs/microservices && docker-compose down && docker-compose pull && docker-compose up -d --force-recreate --always-recreate-deps
# docker image prune -a -f
