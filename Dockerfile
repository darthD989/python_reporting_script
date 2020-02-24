FROM python:3
MAINTAINER LabInfrastructure

USER root

ARG KEY_CERT_DATA

ADD ./ctl_certs.tar.gz /usr/local/share/ca-certificates/
RUN update-ca-certificates

WORKDIR /app
ENV KEY_CERT_DATA $KEY_CERT_DATA
ENV REQUESTS_CA_BUNDLE "/etc/ssl/certs/ca-certificates.crt"
COPY . /app

ADD ./jira_lib.tar.gz /app/

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "./run.py"]
