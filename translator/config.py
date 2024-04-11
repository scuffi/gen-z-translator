import os


class SlackConfig:
    SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
    SLACK_BOT_SIGNING_SECRET = os.environ["SLACK_BOT_SIGNING_SECRET"]


class BotConfig:
    PORT = int(os.environ.get("PORT", 3000))


class OpenAIConfig:
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
