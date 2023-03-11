FROM python:3.8

RUN pip install virtualenv
RUN pip install source
RUN pip install gunicorn[gevent]

RUN python -m venv env
RUN source env/bin/activate
RUN pip install -r requirements.txt

EXPOSE 5000