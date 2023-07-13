import logging
import uvicorn
import time
import random

from typing import Any
from fastapi import FastAPI, Request

logger = logging.getLogger("main")
app = FastAPI()

@app.post("/hello")
def hello_world(request: Request) -> Any:
    actions = [
        {
            "verb": "gather",
            "actionHook": "https://eni9hgp0bdrqn.x.pipedream.net/",
            "input": ["speech"],
            "timeout": 10,
            "recognizer": {
                "vendor": "google",
                "language": "en-US",
            },
            "say": {
                "text": "Thanks for your troubleshooting efforts",
                "synthesizer": {
                    "vendor": "google",
                    "language": "en-US"
                }
            }
        },
        {
            "verb": "gather",
            "actionHook": "https://eni9hgp0bdrqn.x.pipedream.net/",
            "input": ["speech"],
            "timeout": 10,
            "recognizer": {
                "vendor": "google",
                "language": "en-US",
            },
            "say": {
                "text": "This is the 2nd prompt",
                "synthesizer": {
                    "vendor": "google",
                    "language": "en-US"
                }
            }
        },
        {
            "verb": "gather",
            "actionHook": "https://eni9hgp0bdrqn.x.pipedream.net/",
            "input": ["speech"],
            "timeout": 10,
            "recognizer": {
                "vendor": "google",
                "language": "en-US",
            },
            "say": {
                "text": "This is the 3rd prompt",
                "synthesizer": {
                    "vendor": "google",
                    "language": "en-US"
                }
            }
        }
    ]
    return actions


@app.post("/status")
def status(request: Request) -> Any:
    return 200


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("sample.main:app", host="0.0.0.0", port=5000, reload=True)
