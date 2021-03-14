FROM python:3
ENV PYTHONUNBUFFERED=1

RUN mkdir /backend
WORKDIR /backend
COPY requirements.txt /backend/
RUN pip install -r requirements.txt
COPY . /backend/
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
EXPOSE 8000
CMD gunicorn --bind 0.0.0.0:$PORT config.wsgi