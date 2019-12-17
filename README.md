# Elasticsearch cluster in docker

This project provides you with an elasticsearch cluster consisting of three elasticsearch instances.

Make sure you provide docker with enough memory, before you run it with `docker-compose up -d`.

Confirm that elasticsearch is healthy (after a little while) by visiting on of the following:

Elastic search nodes:

- [elasticsearch1](http://localhost:9200/_cat/health)
- [elasticsearch2](http://localhost:9201/_cat/health)
- [elasticsearch3](http://localhost:9202/_cat/health)

Other services:

- [Kibana](http://localhost:5601)

This setup is not meant for production usage, but is very well suited for local integration testing projects and a means of getting to play around with an elasticsearch cluster easily.
