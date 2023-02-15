# Elasticsearch cluster in docker

This project provides you with an elasticsearch cluster consisting of three elasticsearch instances, using the basic license. I've created it during and after the Elastic Engineer training to help me with a ready-to-go environment where I can play with the training labs.

Disclaimer: this setup is not meant for production usage!

## Prerequisites

- A machine with enough RAM (at least 8 gb allocated for the docker environment)
- Docker. (Docker Desktop will suffice for Mac or Windows, but another provider like Rancher Desktop should also work).

## Elasticsearch indices

Some example indices are created at startup:

### `test-index`

Docker container `es-writer` writes data continuously to index `test-index` and reads it using container `es-reader`, all using python scripts and the [official low-level elasticsearch python client library](https://pypi.org/project/elasticsearch/). [View the data](http://localhost:9200/test-index/_search?pretty=true&size=10).

### `blogs`

Example taken from the [Elastic Engineer I training](https://training.elastic.co/instructor-led-training/ElasticsearchEngineerI) containing an excerpt from their online blogs. The index is created (once) from a [csv](logstash-ingest/data/blogs.csv) file using the `logstash-ingest` docker container.
[View the data](http://localhost:9200/blogs/_search?pretty=true&size=1). This is a Static Dataset.

### `logs_server*`

Example taken from the [Elastic Engineer I training](https://training.elastic.co/instructor-led-training/ElasticsearchEngineerI) as well, containing an excerpt from websserver access logs for the [elastic blogs website](https://www.elastic.co/blog/). [View the data](http://localhost:9200/logs_server*/_search?pretty=true&size=1). This is a Time Series Dataset. It can take a while to import this entirely.

## Get it up and running

Make sure you provide docker with enough memory (the default 2gb of memory is not enough, consult your Docker Desktop configuration to change this), before you run it with:

    docker compose up -d

OR

    ./run.sh


    # Stop the services
    ./down.sh

    # Stop the services and clean the volumes. This is useful for starting with a clean slate.
    ./clean.sh

Confirm that elasticsearch is healthy (after a little while) by visiting one of the following links from your browser or a tool like curl or [httpie](https://httpie.org/):

Elastic search nodes:

- [cluster health](http://localhost:9200/_cluster/health?pretty=true)
- [cluster nodes](http://localhost:9200/_nodes/_all/http?pretty=true)
- [elasticsearch1 node health](http://localhost:9200/_cat/health)
- [elasticsearch2 node health](http://localhost:9201/_cat/health)
- [elasticsearch3 node health](http://localhost:9202/_cat/health)

Other services:

- [Kibana](http://localhost:5601)
- [All five indices in Kibana](http://localhost:5601/app/kibana#/management/elasticsearch/index_management/indices?_g=())

## (Optional) Setup security features for Elasticsearch

By default, the Elasticsearch security features are disabled when you have a basic or trial license. To enable security features, use the xpack.security.enabled setting..

_Starting with Elastic Stack 6.8 and 7.1, security features like TLS encrypted communication, role-based access control (RBAC), and more are available for free within the default distribution. In this blog post, we’re going to cover how to get started with using these features to secure your Elasticsearch clusters._

[(source)](https://www.elastic.co/blog/getting-started-with-elasticsearch-security)

## Snapshots

A folder has been bind-mounted to all elasticsearch nodes already with the purpose of sharing snapshots with the docker host. This folder is relative from this directory: `./shared_folder`.
When registering a (fs-type) snapshot repository inside elasticsearch, you should make it point to `/shared_folder` from inside the container.
