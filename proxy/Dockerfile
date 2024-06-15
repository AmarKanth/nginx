FROM nginx

COPY ./entrypoint.sh /entrypoint.sh
COPY ./http.conf /http.conf
COPY ./https.conf /https.conf

RUN chmod +x /entrypoint.sh
RUN chmod +x /http.conf
RUN chmod +x /https.conf