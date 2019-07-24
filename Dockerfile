FROM python:3.6.9-alpine

RUN mkdir -p /opt/app  && \
    mkdir -p /var/log/gunicorn

WORKDIR /opt/app
COPY requirements.txt /opt/app/requirements.txt

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk update && apk add postgresql-dev gcc python3-dev musl-dev \
    && pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /opt/app/requirements.txt

COPY . /opt/app

CMD ["gunicorn", "-w", "4", "-b", ":8000", "run:app"]
