#!/bin/bash
docker build -t wordcloud .
container_id=$(docker run -d wordcloud)
docker wait $container_id
docker cp $container_id:/app/wordcloud.png .
docker rm $container_id
docker image rm wordcloud
