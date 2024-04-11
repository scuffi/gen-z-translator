from logging import Logger

import dotenv

dotenv.load_dotenv()

from config import BotConfig, SlackConfig  # noqa: E402
from searcher import TextSearcher  # noqa: E402
from slack_bolt import App  # noqa: E402

logger = Logger(__name__)

logger.info("Starting bot...")

app = App(
    signing_secret=SlackConfig.SLACK_BOT_SIGNING_SECRET,
    token=SlackConfig.SLACK_BOT_TOKEN,
)

searcher = TextSearcher()


@app.event("app_mention")
def handle_app_mentions(body, say, payload, event):
    say(f"Thanks for the mention <@{event['user']}>!")


@app.event("message")
def handle_message_events(body, say, payload, event):
    say(f"Thanks for the message <@{event['user']}>!")


if __name__ == "__main__":
    logger.info("Running bot")
    app.start(port=BotConfig.PORT)
