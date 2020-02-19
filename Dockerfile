FROM python:slim-buster

RUN apt-get update
RUN apt-get -y install git build-essential openjdk-11-jdk zookeeper
RUN git clone --single-branch --branch ruxton-changes https://github.com/ruxtom/csc8112.git
RUN cd csc8112
RUN pip install -r requirements.txt


# RUN apk add git build-base linux-headers openjdk8
# RUN git clone https://github.com/ruxtom/csc8112.git




# CMD [ "python", "./your-daemon-or-script.py" ]

# WORKDIR /usr/src/app

# CMD [ "python", "./your-daemon-or-script.py" ]