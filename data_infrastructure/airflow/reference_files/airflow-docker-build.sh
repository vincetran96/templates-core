#!/usr/bin/env bash

IMAGE_TAG=something:${1}
ENV=${2}

if [ $ENV == "prod" ]; then
  echo "Building image for PROD environment..."
  USER_ID=10101
  GROUP_ID=10101
elif [ $ENV == "dev" ]; then
  echo "Building image for DEV environment..."
  USER_ID=10001
  GROUP_ID=10001
else
  echo "Building image for LOCAL environment..."
  USER_ID=50000
  GROUP_ID=0
fi

docker build -t $IMAGE_TAG --build-arg user_id=$USER_ID --build-arg group_id=$GROUP_ID -f build/Dockerfile .
