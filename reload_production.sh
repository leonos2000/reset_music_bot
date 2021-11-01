#!/bin/bash
echo "MERGING ENV FILES..."
cat .env.production.base > .env
cat .env.production >> .env
echo "DONE"
echo "BUILDING FRONTEND..."
cd frontend
npm run build >> /dev/null
cd -
echo "DONE"
echo "RESTARTING WEBSERVER SERVICE..."
service music_bot_restart restart >> /dev/null
echo "DONE"