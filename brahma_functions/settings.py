# Settings for Brahma Functions

import os
import openai

DEBUG = True

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API Key
openai.api_key = OPENAI_API_KEY
