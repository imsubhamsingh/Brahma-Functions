# Settings for Brahma Functions

import os
import openai
import pprint

DEBUG = True

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API Key
openai.api_key = OPENAI_API_KEY


def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key
    return True


def list_available_engines():
    """Lists all available engines."""
    return openai.Engine.list()


GPT4 = "gpt-4"
MODEL_NAME = GPT4
model = openai.Model(MODEL_NAME)


def list_accessible_engines():
    """Lists all accessible engines."""
    model_list = openai.Model.list()["data"]
    model_ids = [x["id"] for x in model_list]
    model_ids.sort()
    pprint.pprint(model_ids)


if __name__ == "__main__":
    list_accessible_engines()
