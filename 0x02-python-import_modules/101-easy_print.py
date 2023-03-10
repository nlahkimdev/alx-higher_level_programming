#!/usr/bin/python3
if __name__ == "__main__":
    import logging
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    log = logging.getLogger(__name__)
    log.info('#pythoniscool')
