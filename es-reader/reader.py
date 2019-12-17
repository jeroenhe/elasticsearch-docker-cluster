#!/usr/bin/env python3
import logging
import os
import sys
import time
from datetime import datetime
from elasticsearch import Elasticsearch


LOGGER_FORMAT = '%(asctime)-15s %(message)s'
LOGGER = None
ES_HOST_SEED = os.environ['ES_HOST_SEED'].split(',')


def read_data():
    # https://elasticsearch-py.readthedocs.io/en/master/
    es = Elasticsearch(ES_HOST_SEED, sniff_on_start=True, sniff_on_connection_fail=True,)
    while True:
        # Count the number of records in our index
        # https://www.elastic.co/guide/en/elasticsearch/reference/current/search-count.html
        res_count = es.count(index="test-index")
        LOGGER.info("# of records: %s", res_count['count'])
        
        # Search for the latest record
        # https://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch.Elasticsearch.search
        # https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html
        res = es.search(index="test-index", body={"size": 1, "sort": [{"timestamp": "desc"}], "query": {"match_all": {}}})
        LOGGER.info("Took: %sms, Got %d hits. First hit: %s", res['took'], res['hits']['total']['value'], res['hits']['hits'][0]["_source"])
        time.sleep(5)


def main():
    global LOGGER
    logging.basicConfig(level=logging.INFO, format=LOGGER_FORMAT)
    LOGGER = logging.getLogger('es-writer')
    LOGGER.info("es-writer was started")
    while True:
        try:
            read_data()
        except (KeyboardInterrupt, SystemExit):
            LOGGER.info("Exiting by user request.")
            sys.exit(0)
        except Exception:  # catch *all* exceptions
            LOGGER.error("Fatal error in main loop", exc_info=True)
            sys.exit(1)
        finally:
            LOGGER.info("es-writer was stopped")


if __name__ == "__main__":
    main()
