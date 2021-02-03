#!/bin/bash

docker build -t famass .
docker stop famass
docker rm famass
docker run --name famass -d --env-file /home/ubuntu/famass.env \
  -p 3000:3000 -p 8000:8000 \
  -v /home/ubuntu/dkdata/famass:/dkdata \
  famass start_web.sh
