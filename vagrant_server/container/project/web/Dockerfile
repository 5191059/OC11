
FROM python:3.8.3-buster
USER root

ENV LANGUAGE ja_JP:ja
ENV TZ JST-9
ENV TERM xterm

RUN apt update

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip3 install flask && \
    pip3 install pymysql && \
    pip3 install cryptography　&& \
    pip3 install flask-login && \
    pip3 install argparse && \
    pip3 install beautifulsoup4 && \
    pip3 install requests && \
    pip3 install pymysql && \
    pip3 install html.parser && \
    pip3 install cryptography && \
    pip3 install lxml && \
    pip3 install mysqlclient && \
    pip3 install oauthlib && \
    pip3 install pyOpenSSL && \
    pip3 install gunicorn 

RUN mkdir /worker
RUN mkdir /worker/app
RUN mkdir /worker/app/static
RUN mkdir /worker/app/templates

COPY ./app/db.py /worker/app
COPY ./app/db_con.py /worker/app
COPY ./app/secret.py /worker/app
COPY ./app/testapp.py /worker/app
COPY ./app/User.py /worker/app

COPY ./app/static /worker/app/static
COPY ./app/templates /worker/app/templates
COPY ./config/gunicorn_settings.py /worker/app
COPY ./wait-for-pdb.sh /worker/app/wait-for-pdb.sh


WORKDIR /worker/app

ENTRYPOINT ["gunicorn", "testapp:app"]
CMD [ "--config", "/worker/app/gunicorn_settings.py" ]