#!/usr/bin/env bash
if ! ps aux | grep -v grep | grep -q "backend/dist/server.js"; then
  cd /home/u586615155/domains/2ndpaytech.com/public_html
  nohup /opt/alt/alt-nodejs20/root/usr/bin/node backend/dist/server.js >> backend.log 2>&1 &
fi
