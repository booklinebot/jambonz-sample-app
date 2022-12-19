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
    if random.random() > 0.5:
        time.sleep(60)
    actions = [
        {
            "verb": "say",
            "text": "Hello! This is a sample app for troubleshooting",
            "synthesizer" : {
                "vendor": "Google",
                "language": "en-US"
            }
        }
    ]
    return actions

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("sample.main:app", host="0.0.0.0", port=5000, reload=True)
