# Base Image 
FROM python:3

# setup workdir
WORKDIR /app

# copy all the stuff to app
COPY . /app


# Installing the dependencies
RUN pip3 install -r requirements.txt
EXPOSE 80
EXPOSE 5000

ENTRYPOINT ["uwsgi", "app.ini"]       
