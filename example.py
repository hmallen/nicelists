import configparser
import json
import logging
from pprint import pprint
import sys

from nicemessages.nicemessages import NiceMessages     # When installed: from nicemessages import NiceMessages

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

config_path = '../config/config.ini'

cmc_json_file = 'resources/test_cmc_data.json'


if __name__ == '__main__':
    nice_messages = NiceMessages()

    ## MAIN LOOP ##
    try:
        cmc_data = {}

        with open(cmc_json_file, 'r', encoding='utf-8') as file:
            cmc_data = json.load(file)

        print('CMC Data:')
        pprint(cmc_data)
        print()

        cmc_message = nice_messages.cmc_to_rows(cmc_data)

        cmc_message_nice = nice_messages.even_columns(cmc_message)

        print('Nice Message:')
        print(cmc_message_nice)
        print(type(cmc_message_nice))

    except Exception as e:
        logger.exception('Exception in main loop.')
        logger.exception(e)

    except KeyboardInterrupt:
        logger.info('Exit signal received.')

        sys.exit()
