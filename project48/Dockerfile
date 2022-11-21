FROM python:3.9-bullseye

# set work directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN /usr/local/bin/python -m pip install --upgrade pip

# _________________________________
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
#__________________________________________


COPY . .

## install dependencies
RUN pip3 install -r requirements.txt


RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

EXPOSE 8000
#
CMD python3 manage.py migrate
#CMD python3 manage.py runserver 0.0.0.0:8000