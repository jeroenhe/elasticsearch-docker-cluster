FROM docker.elastic.co/beats/filebeat:8.1.3

USER root

COPY *.sh /
RUN chmod 755 /*.sh

USER filebeat

CMD [ "/run.sh" ]
