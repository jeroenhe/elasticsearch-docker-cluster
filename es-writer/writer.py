#!/usr/bin/env python3
import logging
import os
import random
import sys
import time
from datetime import datetime
from elasticsearch import Elasticsearch


LOGGER_FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOGGER_FORMAT)
LOGGER = logging.getLogger('es-writer')

ES_HOST_SEED = os.environ['ES_HOST_SEED'].split(',')


def write_data():
    # https://elasticsearch-py.readthedocs.io/en/master/
    es = Elasticsearch(ES_HOST_SEED, sniff_on_start=True, sniff_on_node_failure=True)
    counter=-1
    
    while True:
        counter = counter + 1
        doc = {
            'text': 'Random number #' + str(random.randint(1,1000)),
            'timestamp': datetime.now(),
        }
        # https://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch.Elasticsearch.index
        # http://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html

        # when this service restarted, the counter is reset. When a document with the same id already
        # exists, it is updated.
        res = es.index(index="test-index", id=counter, document=doc, op_type="index")

        LOGGER.info("Index result for text '%s': %s", doc['text'], res['result'])
        time.sleep(5)


def main():
    LOGGER.info("es-writer was started")
    while True:
        try:
            write_data()
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
