FROM certbot/certbot

RUN apt-get update && apt-get install -y curl

RUN mkdir -p /scripts

COPY certify-init.sh /scripts/

RUN chmod +x /scripts/certify-init.sh

ENTRYPOINT ["/scripts/certify-init.sh"]