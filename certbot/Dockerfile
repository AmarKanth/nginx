FROM certbot/certbot

COPY certify-init.sh /scripts
RUN chmod +x /scripts/certify-init.sh
ENTRYPOINT ["/scripts/certify-init.sh"]