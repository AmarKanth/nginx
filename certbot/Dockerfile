FROM certbot/certbot

RUN mkdir -p /scripts

COPY certify-init.sh /scripts/

RUN chmod +x /scripts/certify-init.sh

ENTRYPOINT ["/scripts/certify-init.sh"]