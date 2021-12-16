#!/bin/bash

cd ./frontend
npm install -g vue
npm run build
cp -r ./dist ../
cd ../
docker-compose -f compose-build-test.yml up
