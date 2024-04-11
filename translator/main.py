from logging import Logger

import dotenv

dotenv.load_dotenv()

from commands import add_word_command, remove_word_command, update_definition_command
from events import on_mention
from config import BotConfig, SlackConfig  # noqa: E402
from slack_bolt import App  # noqa: E402

logger = Logger(__name__)

logger.info("Starting bot...")

app = App(
    signing_secret=SlackConfig.SLACK_BOT_SIGNING_SECRET,
    token=SlackConfig.SLACK_BOT_TOKEN,
)

# Events
app.event("app_mention")(on_mention)
# TODO: Add option for checking every message


# Commands
app.command("/add-def")(add_word_command)
app.command("/remove-def")(remove_word_command)
app.command("/update-def")(update_definition_command)


if __name__ == "__main__":
    logger.info("Running bot")
    app.start(port=BotConfig.PORT)
