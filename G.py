import os
import logging
import gspread
import modal
from oauth2client.service_account import ServiceAccountCredentials
from slack_sdk.web.client import WebClient
from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler
from pathlib import Path
from dotenv import load_dotenv

'''
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
'''

# To create a logging object
logger = logging.getLogger("Slack_Integration")
logger.setLevel(logging.DEBUG)
log_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
sh = logging.StreamHandler()
sh.setFormatter(log_format)
logger.addHandler(sh)

# Google Sheets credentials and API setup
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)
spreadsheet_key = '1OObSxAxUiMsk300yzMRjDBiVReoBU8sIWj5-EqcIR8M'

# Slack app setup
app = App(token=os.environ.get('SLACK_BOT_TOKEN'))

# Trigger the Shortcut
@app.shortcut('hello-shortcut')
def handle_shortcut(ack, shortcut, client, logger):
    # Acknowledge the shortcut request
    ack()

    client.views_open(
        trigger_id=shortcut["trigger_id"],
        view=modal.diction
    )


# Opening Modal
@app.view("hello-modal")
def handle_submission(ack, body, client, view):
    ack()
    data1 = view["state"]["values"]["block1"]["input1"]["value"]
    data2 = view["state"]["values"]["block2"]["input2"]["value"]
    data3 = view["state"]["values"]["block3"]["input3"]["value"]
    data4 = view["state"]["values"]["block4"]["input4"]["value"]
    data5 = view["state"]["values"]["block5"]["input5"]["value"]
    data6 = view["state"]["values"]["block6"]["input6"]["value"]

    # Write data to Google Spreadsheet
    sheet = gc.open_by_key(spreadsheet_key).sheet1
    sheet.append_row([data1, data2, data3, data4, data5, data6])

    msg = "Your submission was successful"
    try:
        client.chat_postMessage(channel="C05CAG9H162", text=msg)
    except Exception as e:
        logger.exception(f"Failed to post a message {e}")


# Create the SlackRequestHandler for AWS Lambda
slack_request_handler = SlackRequestHandler(app)

# Lambda handler function
def lambda_handler(event, context):
    return slack_request_handler.handle(event, context)
