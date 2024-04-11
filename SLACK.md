# Slack Setup

## Event Handlers

Go to bot settings, then **Event Subscriptions** -> Type in the URL (if using ngrok the ngrok URL) with `/slack/events` at the end of the URL.
Then go down to `Subscribe to bot events` and add the `app_mention` and `message` (can't find this one) events.

## Commands

Create each command, the URL is the same as the event URL
