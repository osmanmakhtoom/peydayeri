FROM python:3.10
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt requirements.txt
RUN pip --timeout=1000 install -r requirements.txt

COPY .. backend
WORKDIR backend

EXPOSE 8000

CMD peydayeri-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - apps.core.wsgi:application