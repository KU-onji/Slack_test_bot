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


def format_to_mrkdwn(text: str) -> str:
    def pre_format(line: str) -> str:
        return line.replace("*", "_")

    def format_list(line: str) -> str:
        if line.startswith("- ") and len(line) > 2:
            return f"・ {line[2:]}"
        else:
            return line

    def format_bold(line: str) -> str:
        return line.replace("__", "*")

    def format_section(line: str) -> str:
        if line.startswith("### ") and len(line) > 4:
            line = line.replace(":\n", "")
            return f"*{line[4:]}*:\n"
        else:
            return line

    li_line = list(map(pre_format, text.splitlines(keepends=True)))
    res = []
    for line in li_line:
        line_formatted = format_list(line)
        line_formatted = format_bold(line_formatted)
        line_formatted = format_section(line_formatted)
        res.append(line_formatted)
    return "".join(res)
