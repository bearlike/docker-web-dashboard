FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
LABEL maintainer="Krishnakanth Alagiri <krishna.alagiri03@gmail.com>"

RUN apk --update add bash nano
COPY requirements.txt /tmp/

# upgrade pip and install required python packages
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

# copy over our app code
COPY ./ /app

# Owner site
ENV OWNER_URL "https://thekrishna.in/"

# Default Credentials
ENV DASH_USERNAME "admin"
ENV DASH_PASSWORD "admin"

EXPOSE 80
