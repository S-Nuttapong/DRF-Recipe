FROM python:3.7-alpine
MAINTAINER Nuttapong Saelek

#running on buffered mode (not allow python to buffer the output, print them directly instead) (reccomend)
ENV PYTHONUNBUFFERED 1 

#copy requirement text from local machine to docker working DIR
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

#create empty DIR called app
RUN mkdir /app
#set app DIR as working DIR
WORKDIR /app
#copy cwd to app(docker working DIR)
COPY ./ /app

#create the user(-D)
RUN adduser -D user
#switch user to 'user' the name of user we just created 
#For security purposes: other wise image will run from root account, if someone compromise our image they can have root access to image and make change to image
#doing this we limit amount of degree of freedom they can do with this image
USER user