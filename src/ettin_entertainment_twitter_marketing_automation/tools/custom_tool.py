from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os

class PostToTwitterInput(BaseModel):
    """Input schema for PostToTwitterTool."""
    tweet_text: str = Field(..., description="The exact text content to be posted to Twitter/X.")

class PostToTwitterTool(BaseTool):
    name: str = "Post to Twitter/X"
    description: str = (
        "A tool that takes text and posts it as a new tweet to the company's Twitter/X account."
    )
    args_schema: Type[BaseModel] = PostToTwitterInput

    def _run(self, tweet_text: str) -> str:
        # This is a simulation. It will just print to your console.
        # It will NOT post to Twitter. This is safer for testing.
        # If you want it to post for real, you would add real Twitter API code here.
        
        print(f"--- SIMULATED TWEET POST ---")
        print(f"Content: {tweet_text}")
        print(f"------------------------------")
        
        return f"SIMULATION: Successfully posted tweet: {tweet_text}"