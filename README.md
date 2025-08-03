#  END TO END Notion MCP Agent

A project to interact with your Notion workspace using natural language commands via Notion MCP, Flask, and Streamlit.


## PREVIEW 

<img width="1748" height="830" alt="Notion MCP Streamlit UI - Google Chrome 8_3_2025 1_40_06 PM" src="https://github.com/user-attachments/assets/e3551a70-17dc-43ce-a491-59fef013c7a9" />



## 🔧 Files Overview

- `port.py` — Starts a test Flask server with ngrok.
- `notion_mcp_agent.py` — Main backend using MCP + LLM agent.
- `final.py` — Production-ready backend for Streamlit.
- `streamlit.py` — Frontend UI using Streamlit.


## TECH Stack

```
Autogen - agentic ai framework
Notion MCP - to access tools form notion
Ngrok - To host your local server publicly
Streamlit - Fornt end
```



## Setup

```bash
git clone https://github.com/yourusername/notion-mcp-agent.git
cd notion-mcp-agent
conda create -p venv 
conda activate venv/
pip install -r requirements.txt
```

ENVIRONMENT FILE 
```
GOOGLE_API_KEY=your_google_key
NOTION_API_KEY=your_notion_key
NGROK_AUTH_TOKEN=your_ngrok_key
```

Run Backend

```
python final.py

```

Run Frontend

```
streamlit run app.py
```

### NOTE :

Run backend first and then frontend , make sure both are running parallely.


### THNAKYOU 

Feel free to contribute

