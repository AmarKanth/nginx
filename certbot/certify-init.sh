#!/bin/sh

# Waits for proxy to be available, then gets the first certificate.

set -e

URL="http://proxy"

while true; do
    HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" $URL)
    
    echo "$HTTP_STATUS"

    if [ $HTTP_STATUS -eq 200 ]; then
        echo "Service is available!"
        break
    else
        echo "Service not available (HTTP status: $HTTP_STATUS). Waiting..."
        sleep 5
    fi
done

echo "Getting certificate..."

DOMAIN=practicepurpose.xyz
EMAIL=amarkanth.bollu@gmail.com
WEBROOT_PATH=/var/www/certbot


if [ -d "/etc/letsencrypt/live/$DOMAIN" ]; then
    certbot renew --webroot -w $WEBROOT_PATH
else
    certbot certonly --webroot -w $WEBROOT_PATH -d $DOMAIN --email $EMAIL --agree-tos --non-interactive
fi