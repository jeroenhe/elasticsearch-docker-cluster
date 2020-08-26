FROM docker.elastic.co/beats/filebeat:7.9.0

USER root

COPY *.sh /
RUN chmod 755 /*.sh

USER filebeat

CMD [ "/run.sh" ]
