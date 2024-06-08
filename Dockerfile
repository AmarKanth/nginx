FROM python:3.9-alpine
RUN apk update && apk add --no-cache python3-dev

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip

RUN apk add --update --no-cache postgresql-client jpeg-dev 
RUN apk add --update --no-cache --virtual .tmp-build-deps build-base postgresql-dev musl-dev zlib zlib-dev linux-headers 
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps
RUN adduser --disabled-password --no-create-home django-user
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN chown -R django-user:django-user /vol
RUN chmod -R 755 /vol
RUN chmod +x entrypoint.sh

USER django-user