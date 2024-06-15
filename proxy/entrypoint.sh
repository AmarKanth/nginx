#!/bin/bash

set -e

echo "Checking for fullchain.pem"
if [ ! -f "/etc/letsencrypt/live/practicepurpose.xyz/fullchain.pem" ]; then
    echo "No SSL cert, enabling HTTP only..."
    cp ./http.conf /etc/nginx/nginx.conf
else
    echo "SSL cert exists, enabling HTTPS..."
    cp ./https.conf /etc/nginx/nginx.conf
fi

nginx-debug -g 'daemon off;'