from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv
import os

load_dotenv()

# Using Google AI Studio
agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp",
                 api_key=os.getenv("GOOGLE_API_KEY"),
                 search=True,
                 ),
    show_tool_calls=True,
    markdown=True,
    monitoring=True
)


# Print the response in the terminal
agent.print_response("why is usa imposing tarrif on other countries?")