#!/bin/bash

docker rm $(docker ps -a -q) && docker rmi pillow-backend
