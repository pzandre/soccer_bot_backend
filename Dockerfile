FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1

RUN apt-get update --fix-missing
RUN apt-get install -y \
    python3-pip \
    python-dev \
    libpq-dev \
    gettext \
    libreadline-dev \
    libssl-dev \
    libjpeg-dev \
    libfreetype6-dev \
    binutils \
    libproj-dev

RUN apt-get autoclean -y \
    clean -y \
    autoremove -y

RUN pip3 install --upgrade pip

RUN mkdir /code
VOLUME /code
ADD . /code
WORKDIR /code

# Install requirements
RUN pip3 install -r requirements.txt
WORKDIR /code

WORKDIR /code

CMD ["python3"]

