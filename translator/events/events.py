from functions import extract_words


def on_mention(body, say, payload, event, client):
    if "thread_ts" not in event:  # Only reply to messages in threads
        return

    # TODO: Add classifier to tell if we want to translate or extract
    if words := _search_words(event, client):
        _create_definition_message(words, say, event["thread_ts"])
    else:
        _no_words_found_message(say, event["thread_ts"])


def _search_words(event, client):
    channel = event["channel"]
    thread_ts = event["thread_ts"]
    history = client.conversations_replies(channel=channel, ts=thread_ts)
    message = history["messages"][0]

    return extract_words(message["text"])


def _create_definition_message(words, say, thread):
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
                "text": "Someone used some words you're not familiar with? I'll try define them for you:",
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

    say(text="", blocks=response, thread_ts=thread, mrkdwn=True)


def _no_words_found_message(say, thread):
    say(
        text="I can't find any Gen Z lingo in that message, maybe it's event too young for me...",
        thread_ts=thread,
    )
