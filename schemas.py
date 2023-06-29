"""
Schemas for OpenAI Function Calling
"""

reddit_schema = {
  "type": "object",
  "properties": {
    "links": {
      "type": "array",
      "items": {"type": "string"},
      "minItems": 5,
      "maxItems": 10,
      "description": "URL to subreddit from reddit.com related to the topic provided. These are real sites. Do not make up URLs."
    }
  },
  "required": ["links"]
}

tweet_schema = {
  "type": "object",
  "properties": {
    "tweets": {
      "type": "array",
      "items": {"type": "string"},
      "minItems": 5,
      "maxItems": 10,
      "description": "Short messages about the content of this blog post that can be posted on Twitter. This message cannot be longer than 280 total characters.",
      "maxLength": 280
    },
    "hashtags": {
      "type": "array",
      "items": {"type": "string"},
      "minItems": 1,
      "maxItems": 5,
      "description": "Hashtags related to the tweet message.",
    },
    "emojis": {
      "type": "array",
      "items": {"type": "string"},
      "minItems": 1,
      "maxItems": 5,
      "description": "Emojis related to the tweet message.",
    }
  },
  "required": ["tweets", "hashtags", "emojis"]
}

class Schemas:
    def __init__(self):
        self.reddit_schema = reddit_schema
        self.tweet_schema = tweet_schema
