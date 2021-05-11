FROM mcr.microsoft.com/azure-functions/python:3.0-python3.8

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

# install all the dependencies
RUN apt-get -y update \
    && apt-get install -y \
        build-essential \
        python3-dev \
        python3-pip \
        python3-setuptools \
        python3-wheel \
        python3-cffi \
        libcairo2 \
        libpango-1.0-0 \
        libpangocairo-1.0-0 \
        libgdk-pixbuf2.0-0 \
        libffi-dev shared-mime-info \
    && apt-get -y clean

COPY requirements.txt ./

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . /home/site/wwwroot