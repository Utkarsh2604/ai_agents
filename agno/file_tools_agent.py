from agno.agent import Agent
from agno.tools.file import FileTools
from agno.tools.local_file_system import LocalFileSystemTools
import os
from agno.models.google import Gemini

from dotenv import load_dotenv
load_dotenv()
from pathlib import Path

from typing import Iterator
from agno.agent import Agent, RunResponse
from agno.utils.pprint import pprint_run_response

path = Path.cwd().joinpath("files")
agent = Agent(model=Gemini(id="gemini-2.0-flash",api_key=os.getenv("GOOGLE_API_KEY")),
              tools=[LocalFileSystemTools(target_directory=path),FileTools(Path(path),save_files=True)], 
              show_tool_calls=True,debug_mode=True,telemetry=False,
              monitoring=False)
# response = agent.print_response("What is the most advanced LLM currently?",stream=True,)

# Run agent and return the response as a variable
response: RunResponse = agent.run("give me a pydantic model for blog and give me a prompt to feed my agent to create short blogs based on pydantic model?")

# # Run agent and return the response as a stream
# response_stream: Iterator[RunResponse] = agent.run("Tell me a 5 second short story about a lion", stream=True)

# Print the response in markdown format
pprint_run_response(response, markdown=True)

# Print the response stream in markdown format
# pprint_run_response(response_stream, markdown=True)


# 1st method 
result = LocalFileSystemTools(target_directory=path)
result.write_file(content=response.content,filename="test.txt")

# 2nd method
result = FileTools(path,save_files=True)
result.save_file(contents=response.content,file_name="testt.txt")

