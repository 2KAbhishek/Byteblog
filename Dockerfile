FROM python:3.6-alpine

RUN adduser -D byteblog

WORKDIR /home/byteblog

COPY requirements.txt requirements.txt
RUN python -m venv dev
RUN dev/bin/pip install -r requirements.txt
RUN dev/bin/pip install gunicorn pymysql

COPY app app
COPY migrations migrations
COPY byteblog.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP byteblog.py

RUN chown -R byteblog:byteblog ./
USER byteblog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
