import logging
from pprint import pprint
import sys

#logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class NiceMessages:
    def __init__(self):
        pass


    def cmc_to_rows(self, cmc_data):
        cmc_message = ''

        cmc_message += '*Name:* ' + cmc_data['name'] + '\n'
        cmc_message += '*Market Cap:* ' + str(cmc_data['markets_cap']) + '\n'
        cmc_message += '*Rank:* #' + str(cmc_data['rank']) + '\n'
        cmc_message += '*24h Volume:* ' + str(cmc_data['markets_volume_24h']) + '\n'
        cmc_message += '*Price:* ' + str(cmc_data['price']) + '\n'
        if cmc_data['source_code'] != None:
            cmc_message += '*Source Code:* ' + cmc_data['source_code'] + '\n'

        if len(cmc_data['webs']) > 0:
            cmc_message += '*Websites:*' + '\n'

            for site in cmc_data['webs']:
                #if '\n' in site:
                    #logger.error('SITE')
                    #sys.exit(1)

                if site != '':
                    cmc_message += '    ' + site + '\n'

        if len(cmc_data['message_boards']) > 0:
            cmc_message += '*Message Boards:*' + '\n'

            for board in cmc_data['message_boards']:
                #if '\n' in board:
                    #logger.error('BOARD')
                    #sys.exit(1)

                if board != '':
                    cmc_message += '    ' + board + '\n'

        if len(cmc_data['chats']) > 0:
            cmc_message += '*Chats:*' + '\n'

            for chat in cmc_data['chats']:
                #if '\n' in chat:
                    #logger.error('CHAT')
                    #sys.exit(1)

                if chat != '':
                    cmc_message += '    ' + chat + '\n'

        if len(cmc_data['explorers']) > 0:
            cmc_message += '*Explorers:*' + '\n'

            for explorer in cmc_data['explorers']:
                #if '\n' in explorer:
                    #logger.error('EXPLORER')
                    #sys.exit(1)

                if explorer != '':
                    cmc_message += '    ' + explorer + '\n'

        return cmc_message


    def even_columns(self, input_text):
        colon_idx_min = None
        colon_idx_max = None

        row_list = input_text.split('\n')

        while (True):   # NEED MORE ELEGANT SOLUTION FOR THIS?
            if '' in row_list:
                row_list.remove('')

            else:
                break

        row_data = []

        #for row in row_list:
        for x in range(0, len(row_list)):
            row = row_list[x]
            logger.debug('[IDX] row: ' + row)

            if 'Websites' not in row and 'Chats' not in row and 'Explorers' not in row and 'http' not in row:
                colon_idx = row.index(':')

                if colon_idx_min == None or colon_idx < colon_idx_min:
                    colon_idx_min = colon_idx

                if colon_idx_max == None or colon_idx > colon_idx_max:
                    colon_idx_max = colon_idx

            else:
                colon_idx = -1

            row_data.append((row, colon_idx))

        colon_idx_max += 1      # To account for the space occupied by the Slack message formatter "*"

        logger.debug('Colon Index Min: ' + str(colon_idx_min))
        logger.debug('Colon Index Max: ' + str(colon_idx_max))

        rows_nice = []

        for row in row_data:
            logger.debug('[MOD] row: ' + str(row))

            row_modified = ''

            #if 'Websites' not in row and 'Chats' not in row and 'Explorers' not in row:
            if row[1] != -1:
                for x in range(0, len(row[0])):
                    row_modified += row[0][x]

                    if x == (row[1] + 1):
                        for x in range(0, (colon_idx_max - row[1])):
                            row_modified += ' '

                        #row_modified += ':'

            else:
                row_modified = row[0]

            #logger.debug('row_modified: ' + row_modified)

            rows_nice.append(row_modified)

        output_text = ''

        for row in rows_nice:
            output_text += row + '\n'

        #output_text.rstrip('\n')

        return output_text


if __name__ == '__main__':
    nice_messages = NiceMessages()

    test_file = 'test_cmc_message.txt'

    with open(test_file, 'r', encoding='utf-8') as file:
        sample_data = file.read()

    print('Input Data:')
    print(sample_data)

    print()

    sample_data_nice = nice_messages.even_columns(input_text=sample_data)

    print('Nice Message:')
    print(sample_data_nice)
