# Elasticsearch cluster in docker

This project provides you with an elasticsearch cluster consisting of three elasticsearch instances.

## Indices

Example indices created:

### `test-index`

Docker container `es-writer` writes data continuously to index `test-index` and reads it using container `es-reader`.

### `blogs`

Example taken from the [Elastic Engineer I training](https://training.elastic.co/instructor-led-training/ElasticsearchEngineerI) containing an excerpt from their online blogs. The index is created (once) from a [csv](logstash-ingest/data/blogs.csv) file using the `logstash-ingest` docker container.
[View the data](http://localhost:9200/blogs/_search?pretty=true&size=1). This is a Static Dataset.

### `logs_server*`

Example taken from the [Elastic Engineer I training](https://training.elastic.co/instructor-led-training/ElasticsearchEngineerI) as well, containing an excerpt from websserver access logs for the [elastic blogs website](https://www.elastic.co/blog/). This is a Time Series Dataset.

## Get it up and running

Make sure you provide docker with enough memory, before you run it with `docker-compose up -d`.

Confirm that elasticsearch is healthy (after a little while) by visiting on of the following:

Elastic search nodes:

- [cluster health](http://localhost:9200/_cluster/health?pretty=true)
- [elasticsearch1](http://localhost:9200/_cat/health)
- [elasticsearch2](http://localhost:9201/_cat/health)
- [elasticsearch3](http://localhost:9202/_cat/health)

Other services:

- [Kibana](http://localhost:5601)
- [All five created indices in Kibana](http://localhost:5601/app/kibana#/management/elasticsearch/index_management/indices?_g=())

## Setup Security

_By default, the Elasticsearch security features are disabled when you have a basic or trial license. To enable security features, use the xpack.security.enabled setting._

Code:

    # https://www.elastic.co/blog/getting-started-with-elasticsearch-security
    bin/elasticsearch-certutil cert -out config/elastic-certificates.p12 -pass ""
    xpack.security.enabled: true
    xpack.security.transport.ssl.enabled: true
    xpack.security.transport.ssl.verification_mode: certificate
    xpack.security.transport.ssl.keystore.path: elastic-certificates.p12
    xpack.security.transport.ssl.truststore.path: elastic-certificates.p12


This setup is not meant for production usage, but is very well suited for local integration testing projects and a means of getting to play around with an elasticsearch cluster easily.
