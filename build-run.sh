#!/bin/bash
app="krishna/docker-cluster-dash"
cont_name="cluster-dash-dev01"

docker rm -f ${cont_name} || true
docker build -t ${app} .
docker run -d -p 56733:80 --name=${cont_name} ${app}