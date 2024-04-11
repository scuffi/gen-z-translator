from functions import extract_words


def on_mention(body, say, payload, event, client):
    if "thread_ts" not in event:  # Only reply to messages in threads
        return

    # TODO: Add classifier to tell if we want to translate or extract
    channel = event["channel"]
    original_thread_ts = event["thread_ts"]
    history = client.conversations_replies(channel=channel, ts=original_thread_ts)
    message = history["messages"][0]["text"]

    words = extract_words(message)

    thread_ts = event["thread_ts"]
    say(text=f"{words}", thread_ts=thread_ts)
