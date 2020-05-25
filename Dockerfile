FROM mongo:latest


RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 python3-pip \
	cron \
	curl wget \
	supervisor \
	vim
RUN pip3 install \
	requests \
	pymongo \
	feedparser

CMD [ "useradd --create-home scrapper" ]

COPY project/cron/scrapper_cron /etc/cron.d/scrapper_cron
CMD [ "chmod ugo+x /etc/cron.d/" ]

COPY ./project/conf/mongod.conf /etc/

#COPY ./project/cron/scrapper_cron /var/spool/cron/crontabs/root
COPY ./project/main.py /home/scrapper/
COPY ./project/conf/supervisor.conf /etc/supervisor/conf.d/supervisor.conf


#CMD service rsyslog start && service cron start && tail -f /var/log/syslog
CMD /usr/bin/supervisord
