import configparser
import json
import logging
from pprint import pprint
import sys

from slackclient import SlackClient

from nicemessages.nicemessages import NiceMessages     # When installed: from nicemessages import NiceMessages

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

config_path = '../config/config.ini'

cmc_json_file = 'test_cmc_data.json'


def send_slack_alert(channel_id, message):
    alert_result = True

    alert_return = {}

    try:
        """
        attachment_array =  [{"fallback": "Resistance/Support Chart (Fallback)",
                              "color": "#36a64f",
                              "pretext": "Resistance/Support Chart (Pretext)",
                              "title": "Resistance/Support Chart (Title)",
                              "title_link": s3_url_html,
                              "image_url": s3_url_png,
                              "thumb_url": s3_url_png}]#,
                              #"ts": 123456789}]

        attachments = json.dumps(attachment_array)
        """

        print(message)

        alert_return = slack_client.api_call(
            'chat.postMessage',
            channel=channel_id,
            text=message,
            #text=message_json,
            username=slack_bot_user,
            #icon_emoji=slack_alert_user_icon,
            icon_url=slack_bot_icon,
            #attachments=attachments
        )

    except Exception as e:
        logger.exception('Exception while sending Slack alert.')
        logger.exception(e)

        alert_result = False

    finally:
        return alert_result, alert_return


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read(config_path)

    slack_token = config['slack']['slack_token']

    slack_channel_testing = config['settings']['slack_channel_testing']

    slack_bot_user = config['settings']['slack_bot_user']
    slack_bot_icon = config['settings']['slack_bot_icon']

    # Slack connection
    slack_client = SlackClient(slack_token)

    channel_list = slack_client.api_call('channels.list')
    group_list = slack_client.api_call('groups.list')

    slack_channel_targets = {'testing': slack_channel_testing}

    for target in slack_channel_targets:
        try:
            logger.debug('channel_list.get(\'ok\'): ' + str(channel_list.get('ok')))
            if channel_list.get('ok'):
                for chan in channel_list['channels']:
                    logger.debug('chan[\'name\']: ' + chan['name'])
                    if chan['name'] == slack_channel_targets[target]:
                        if target == 'public':
                            slack_channel_id_public = chan['id']

                        elif target == 'private':
                            slack_channel_id_private = chan['id']

                        elif target == 'testing':
                            slack_channel_id_testing = chan['id']

                        elif target == 'exceptions':
                            slack_channel_id_exceptions = chan['id']

                        break
                else:
                    logger.error('No valid Slack channel found for alert in channel list.')

                    sys.exit(1)

            else:
                logger.error('Channel list API call failed.')

                sys.exit(1)

        except:
            logger.debug('group_list.get(\'ok\'): ' + str(group_list.get('ok')))
            if group_list.get('ok'):
                for group in group_list['groups']:
                    logger.debug('group[\'name\']: ' + group['name'])
                    if group['name'] == slack_channel_targets[target]:
                        if target == 'public':
                            slack_channel_id_public = group['id']

                        elif target == 'private':
                            slack_channel_id_private = group['id']

                        elif target == 'testing':
                            slack_channel_id_testing = group['id']

                        elif target == 'exceptions':
                            slack_channel_id_exceptions = group['id']

                        break
                else:
                    logger.error('No valid Slack channel found for alert in group list.')

                    sys.exit(1)

            else:
                logger.error('Group list API call failed.')

                sys.exit(1)

    logger.info('Slack channel for testing: #' + slack_channel_testing +
                ' (' + slack_channel_id_testing + ')')

    nice_lists = NiceLists()

    ## MAIN LOOP ##
    try:
        cmc_data = {}

        with open(cmc_json_file, 'r', encoding='utf-8') as file:
            cmc_data = json.load(file)

        print('CMC Data:')
        pprint(cmc_data)
        print()

        cmc_message = nice_lists.cmc_to_rows(cmc_data)

        cmc_message_nice = nice_lists.even_columns(cmc_message)

        print('Nice Lists:')
        print(cmc_message_nice)
        print(type(cmc_message_nice))

        #alert_result, alert_return = send_slack_alert(slack_channel_id_testing, cmc_message_nice)
        alert_result, alert_return = send_slack_alert(slack_channel_id_testing, cmc_message)

        logger.debug('alert_result: ' + str(alert_result))

        print('Alert Return:')
        pprint(alert_return)

    except Exception as e:
        logger.exception('Exception in main loop.')
        logger.exception(e)

    except KeyboardInterrupt:
        logger.info('Exit signal received.')

        sys.exit()
