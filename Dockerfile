FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /docker_app

# RUN apt update

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

RUN mkdir ./static 

RUN rm ./db.sqlite3

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate

RUN python3 manage.py collectstatic --noinput

ENV PORT 8000

RUN echo ${PORT}

EXPOSE $PORT 

# VOLUME [ "/docker_app/logged_details" ]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
