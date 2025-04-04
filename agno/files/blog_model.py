from pydantic import BaseModel, Field
from typing import List

class Blog(BaseModel):
    title: str = Field(..., description="Title of the blog post")
    content: str = Field(..., description="Main content of the blog post")
    author: str = Field(..., description="Author of the blog post")
    tags: List[str] = Field(..., description="List of tags associated with the blog post")
    publication_date: str = Field(..., description="Date when the blog post was published (YYYY-MM-DD)")