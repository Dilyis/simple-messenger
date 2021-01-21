FROM python:3.7.5-alpine3.9

ENV PYTHONPATH=${PYTHONPATH}:/app
RUN rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*
RUN apk update && apk add --no-cache --virtual build-dependencies gcc make libc-dev python3-dev build-base linux-headers pcre-dev curl && \
    apk add --no-cache postgresql-dev jpeg-dev zlib-dev libressl-dev libffi-dev postgresql-client gettext
COPY ./app /app
WORKDIR /app
RUN pip install -U pip && pip install pipenv && \
    pipenv lock --requirements > requirements.txt && \
    pip install --no-cache-dir -r requirements.txt && \
    rm /app/Pipfile && \
    rm /app/Pipfile.lock
CMD ["python3"]
