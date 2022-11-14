FROM python:3.9-bullseye
#FROM python:3.11
#FROM kuralabs/python3-dev

#WORKDIR /usr/src/app
#COPY environprinter.py ./
#CMD [ "python3", "./environprinter.py" ]
#


# set work directory
RUN mkdir -p /crm_user/src/app
WORKDIR /crm_user/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /crm_user/src/app

RUN /usr/local/bin/python -m pip install --upgrade pip

# _________________________________
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
#__________________________________________



## install dependencies
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD python3 manage.py migrate
#CMD python manage.py createsuperuser
#CMD python manage.py startproject
CMD python3 manage.py runserver 0.0.0.0:8000