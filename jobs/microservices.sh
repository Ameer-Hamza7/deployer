#!/bin/bash
docker login
cd /root/xtremeanalytix/deployer/deployer/jobs/microservices && docker-compose pull $1 && docker-compose up -d --force-recreate --always-recreate-deps
docker image prune -a -f
