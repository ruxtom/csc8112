FROM python:3.7-alpine
RUN apk add git
RUN git clone https://github.com/ruxtom/csc8112.git
RUN cd csc8112
RUN pip install

# CMD [ "python", "./your-daemon-or-script.py" ]

# WORKDIR /usr/src/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# CMD [ "python", "./your-daemon-or-script.py" ]