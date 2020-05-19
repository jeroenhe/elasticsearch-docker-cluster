FROM docker.elastic.co/logstash/logstash:7.7.0

USER root

COPY *.sh /
RUN chmod 755 /*.sh

USER logstash
COPY logstash.yml /usr/share/logstash/config/logstash.yml

CMD [ "/run.sh" ]
