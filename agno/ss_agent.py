from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv
import os

from agno.tools.googlesearch import GoogleSearchTools

load_dotenv()

# Using Google AI Studio
agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp",
                 api_key=os.getenv("GOOGLE_API_KEY"),
                 search=True
                 ),
    # tools=[GoogleSearchTools()],
    show_tool_calls=True,
    # markdown=True,
    monitoring=False,
    telemetry=False,
    debug_mode=True,
    save_response_to_file="./files/india.txt",
)


# Print the response in the terminal
# agent.print_response("Give Me a pydantic model for blog and give me a prompt to feed my agent to create short blogs based on pydantic model?",stream=True)
agent.print_response("Give Me India History Facts",stream=True)


#either use gemini inbuilt search or use google search tools