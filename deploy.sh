#!/usr/bin/env bash

set -x
set -e

npm install
npm run build
git add dist --force
git commit -m "Deploy"
git branch -D gh-pages || : # delete if there
git subtree split HEAD --prefix dist -b gh-pages 
git reset --hard HEAD~1 
git push origin gh-pages --force
