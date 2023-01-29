FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /docker_app

# RUN apt update

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
