AI Agent for Population Queries

This is a small project where I built an AI agent that can answer questions about world population using a dataset (CSV file). The agent uses a powerful LLM (LLaMA-3 from Groq) and converts natural language queries into code that runs on the data.

### What it does:

- Loads a population dataset from CSV
- Lets users ask questions like “What’s the total population of Asia?” or “Which country has the highest population?”
- Uses a language model to convert the question into pandas code
- Runs the code on the data and gives the answer
- Supports multiple tools that can be used by the AI depending on the question

### How it works:

- I used the `llama-index` library to build the agent
- The model (from Groq) understands the query and turns it into pandas expressions
- I set up prompts and custom instructions to guide how the model should behave
- The environment variable (GROQ API key) is safely stored in a `.env` file and not pushed to GitHub

### Technologies Used:

- Python
- Pandas
- llama-index
- Groq LLM (LLaMA-3)
- dotenv

### Notes:

- The `.env` file is ignored and not part of the repo
- This is a simple proof-of-concept project to test how agents work with structured data

