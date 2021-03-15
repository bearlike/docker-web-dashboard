FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
LABEL maintainer="Krishnakanth Alagiri <krishna.alagiri03@gmail.com>"

RUN apk add --no-cache "mongodb~=3.4.10"

# upgrade pip and install supervisor (release date: Feb 27, 2021)
RUN pip install supervisor==4.2.2 && \
    mkdir -p /var/log/supervisor && \
    mkdir -p /etc/supervisor/conf.d

VOLUME /data/db

COPY requirements.txt /tmp/

# install required python packages
RUN pip install -r /tmp/requirements.txt

# copy over our app code
COPY ./ /app

# Owner site
ENV OWNER_URL "https://thekrishna.in/"

# Default Credentials
ENV DASH_USERNAME "admin"
ENV DASH_PASSWORD "admin"

EXPOSE 80

# supervisor base configuration
COPY supervisor.conf /etc/supervisor.conf

# default command
CMD ["supervisord", "-c", "/etc/supervisor.conf"]