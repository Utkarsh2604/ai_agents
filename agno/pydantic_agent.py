import json
import os
from pathlib import Path
from typing import Iterator
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List

load_dotenv()

from agno.agent import Agent
from agno.utils.pprint import pprint_run_response
from agno.models.google import Gemini
path = Path.cwd().joinpath("files")


class Blog(BaseModel):
    title: str = Field(..., description="Title of the blog post")
    content: str = Field(..., description="Main content of the blog post")
    author: str = Field(..., description="Author of the blog post")
    tags: List[str] = Field(..., description="List of tags associated with the blog post")
    publication_date: str = Field(..., description="Date when the blog post was published (YYYY-MM-DD)")



# Agent that uses structured outputs
blog_agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp",api_key=os.getenv("GOOGLE_API_KEY")),
    show_tool_calls=True,
    debug_mode=False,
    telemetry=False,
    monitoring=False,
    description="You write blogs for a living. You are an expert in writing blogs. You can write blogs on any topic. You can also write blogs in different styles. You can also write blogs in different formats. You can also write blogs in different languages.",
    response_model=Blog,
    add_history_to_messages=True,
    add_datetime_to_instructions=True,
    # use_json_mode=True,
    save_response_to_file="./files/blog_response.json",
    
)


response =  blog_agent.run("Latest Trends In Generative AI")

pprint_run_response(response, markdown=True)


print(response.metrics)





