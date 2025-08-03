#  REFERENCES 
   
# https://developers.notion.com/docs/get-started-with-mcp

# https://github.com/makenotion/notion-mcp-server?tab=readme-ov-file

import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, mcp_server_tools
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

import os

notion_secret = os.getenv("NOTION_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["NOTION_API_KEY"] = notion_secret

SYSTEM_MESSAGE = """

You are a helpful assistant that can search and summarize 
content from the user's Notion workspace and also list what is asked.
Try to assume the tool and call the same and get the answer. 
Say TERMINATE when you are done with the task.

"""

async def config():
    
    params = StdioServerParams(
        command="C:/Program Files/nodejs/npx.cmd",
        args=['-y','mcp-remote','https://mcp.notion.com/mcp'],
        env={
            'NOTION_API_KEY':notion_secret
        },
        read_timeout_seconds=20
    )
    
    model = OpenAIChatCompletionClient(
        model="gemini-2.5-flash",
        api_key=openai_api_key,
    )

    mcp_tools= await mcp_server_tools(server_params=params)
    
    agent= AssistantAgent(
        name='notion_agent',
        system_message=SYSTEM_MESSAGE,
        model_client=model,
        tools=mcp_tools,
        reflect_on_tool_use=True
    )
    
    team = RoundRobinGroupChat(
        participants=[agent],
        max_turns=5,
        termination_condition=TextMentionTermination('TERMINATE')
    )
    
    return team

async def orchestrate(team, task):
    async for msg in team.run_stream(task=task):
        yield msg 

async def main():
    team = await config()
    task = "Create a new page titled 'PAGE BANA DE BROO' "

    async for msg in orchestrate(team, task):
        print("*" * 40)
        print(msg)
        print("=" * 40)

if __name__ == "__main__":
    asyncio.run(main())