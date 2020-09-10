FROM python:3.8

MAINTAINER Jerome <jkpaddick@gmail.com>

COPY . /usr/src/flask_app
WORKDIR /usr/src/flask_app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/usr/src/flask_app/server.py"]