from functions import extract_words


def on_mention(body, say, payload, event, client):
    if "thread_ts" not in event:  # Only reply to messages in threads
        return

    # TODO: Add classifier to tell if we want to translate or extract
    channel = event["channel"]
    thread_ts = event["thread_ts"]
    history = client.conversations_replies(channel=channel, ts=thread_ts)
    message = history["messages"][0]

    words = extract_words(message["text"])

    words_list = "".join(f"> *{word}* - _{definition}_\n" for word, definition in words)

    response = [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": ":wave: *Hello millenials!*"},
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"<@{message['user']}> used some words you're not familiar with? I'll try define them for you:",
            },
        },
        {"type": "section", "text": {"type": "mrkdwn", "text": f"{words_list}"}},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "_I hope that helps in understanding the message. If not, I can try to translate into the real English._",
            },
        },
    ]

    say(text="", blocks=response, thread_ts=thread_ts, mrkdwn=True)
