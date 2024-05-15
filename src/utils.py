import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


def create_app_socketModeHandler():
    app_token = os.getenv("SLACK_APP_TOKEN_TEST")
    bot_token = os.getenv("SLACK_BOT_TOKEN_TEST")
    app = App(token=bot_token)
    return app, SocketModeHandler(app=app, app_token=app_token)


def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as f:
        return f.read()
