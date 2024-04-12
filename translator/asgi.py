"""
This file is only for running through Docker.

It uses a FastAPI/Gunicorn server to handle requests.

If you are running locally, just running `python3 app.py` should work.
"""

from fastapi import FastAPI, Request

# Local import from main -> Only for docker deployment
from main import app
from slack_bolt.adapter.fastapi import SlackRequestHandler

api = FastAPI()

app_handler = SlackRequestHandler(app)  # TODO: Should this be AsyncApp instead?


@api.post("/slack/events")
async def endpoint(req: Request):
    return await app_handler.handle(req)
