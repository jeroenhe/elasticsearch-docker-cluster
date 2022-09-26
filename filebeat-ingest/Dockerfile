ARG ELASTIC_VERSION
FROM docker.elastic.co/beats/filebeat:${ELASTIC_VERSION}

USER root

COPY *.sh /
RUN chmod 755 /*.sh

USER filebeat

CMD [ "/run.sh" ]
