import re

from utils import create_app_socketModeHandler, read_txt

app, handler = create_app_socketModeHandler()


@app.message(keyword=re.compile(r"^test$"))
def post_test_message(body):
    main_event = body["event"]
    channel = main_event["channel"]
    summary = read_txt("pdfs/summary.txt")
    app.client.chat_postMessage(
        channel=channel, text=summary, blocks=[{"type": "section", "text": {"type": "mrkdwn", "text": summary}}]
    )


if __name__ == "__main__":
    handler.start()
