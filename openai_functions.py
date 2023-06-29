"""Functions for OpenAI ChatCompletion"""
from openai_schemas import Schemas

functions = [
    {
        "name": "create_tweet", 
        "description": "Tweet data for twitter based on a given topic.",
        "parameters": Schemas().tweet_schema
    },
    {
        "name": "related_subreddits",
        "description": "List of the top subreddits from reddit based on the topic provided.",
        "parameters": Schemas().reddit_schema
    },
]

class Functions:
    def __init__(self):
        self.functions = functions
