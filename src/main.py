import re

from utils import create_app_socketModeHandler, format_to_mrkdwn, read_txt

app, handler = create_app_socketModeHandler()


@app.message(re.compile(r"^testApp$"))
def post_test_message(body):
    main_event = body["event"]
    channel = main_event["channel"]
    summary = read_txt("pdfs/summary.txt")
    summary_formatted = format_to_mrkdwn(summary)
    app.client.chat_postMessage(
        channel=channel,
        text=summary,
        thread_ts=main_event["ts"],
        blocks=[{"type": "section", "text": {"type": "mrkdwn", "text": summary_formatted}}],
    )
    print("Message from testApp.")


if __name__ == "__main__":
    handler.start()
