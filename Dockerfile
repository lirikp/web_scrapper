FROM mongo:latest


RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 python3-pip
#RUN apt-get install -y mongodb

#CMD [ "python"]
