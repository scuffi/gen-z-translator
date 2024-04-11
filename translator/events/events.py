from functions import extract_words, get_category, translate_message


def on_mention(body, say, payload, event, client):
    if "thread_ts" not in event:  # Only reply to messages in threads
        return

    category = get_category(event["text"])

    print(category)

    words = _search_words(event, client)

    if category == "define":
        if words:
            _create_definition_message(words, say, event["thread_ts"])
        else:
            _no_words_found_message(say, event["thread_ts"])

    elif category == "translate":
        _send_translate_message(
            event,
            say,
            client,
        )


def _get_thread_message(event, client):
    channel = event["channel"]
    thread_ts = event["thread_ts"]
    history = client.conversations_replies(channel=channel, ts=thread_ts)
    return history["messages"][0]


def _search_words(event, client):
    message = _get_thread_message(event, client)

    return extract_words(message["text"])


def _create_definition_message(words, say, thread):
    words_list = "".join(f"> *{word}* - _{definition}_\n" for word, definition in words)

    response = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": ":wave: Hello millenial!",
                "emoji": True,
            },
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


def _send_translate_message(event, say, client):
    translated = translate_message(_get_thread_message(event, client)["text"])

    response = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "This lingo too young for you? Here's a an _older_ translation:",
            },
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"> {translated}",
            },
        },
    ]

    say(text="", blocks=response, thread_ts=event["thread_ts"], mrkdwn=True)
