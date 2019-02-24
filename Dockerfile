FROM python:3.6-stretch
LABEL maintainer="John Ruiz <jruiz@johnruiz.com>"

RUN pip install pipenv pytest flake8 && \
  mkdir -p /data/wemoctl

WORKDIR /data/wemoctl
COPY ./ /data/wemoctl/

RUN /data/wemoctl/script/bootstrap && \
  ln -s /data/wemoctl/wemoctl /usr/local/bin/wemoctl
