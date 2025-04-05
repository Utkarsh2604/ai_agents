from agno.agent import Agent

from agno.models.google import Gemini
from agno.embedder.google import GeminiEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.chroma import ChromaDb


from dotenv import load_dotenv
import os

import typer
from rich.prompt import Prompt
from typing import Optional

load_dotenv()


knowledge=PDFUrlKnowledgeBase(
            urls=["https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf"],
            vector_db=ChromaDb(
                path="./files/",
                embedder=GeminiEmbedder(api_key=os.getenv("GOOGLE_API_KEY")),
                collection="Attention",
            ),
        )


def agent_run(user: str = "user"):
    agent = Agent(
        model=Gemini(id="gemini-2.0-flash-exp", api_key=os.getenv("GOOGLE_API_KEY"),search=False,
                    ),
        description="You are an Artifical Intelligence, Machine Learning expert!",
        instructions=[
            "Search your knowledge base for User Query Regarding to Topics given in pdf",
            "Prefer the information in your knowledge base.",
            "Attetion Is All you need is the topic of the pdf",
            "You are an expert in your field, so answer the question with confidence.",
        ],
        show_tool_calls=True,
        # markdown=True,
        telemetry=False,
        monitoring=False,
        debug_mode=True,
        save_response_to_file='./files/attetion.txt',
    )
    
    while True:
        message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
        if message in ("exit", "bye"):
            break
        agent.print_response(message)


if __name__ == "__main__":
    
    knowledge.load(recreate=False)
        
    typer.run(agent_run)
        
        
    
# agent.print_response("What is the paper about? give me a detailed response", stream=True)
# agent.print_response("What is transformer?",markdown=True)