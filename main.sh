#!/bin/bash
echo 'hello before'
source venv/bin/activate && python deploy_jobs.py
echo 'hello after'
