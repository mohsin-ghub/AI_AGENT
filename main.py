from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from llama_index.llms.groq import Groq
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent



load_dotenv()


groq_api_key = os.getenv("GROQ_API_KEY")


llm = Groq(
    model="llama3-8b-8192",  
    api_key=groq_api_key,
)

population_path = os.path.join("data", "population.csv")
population_df = pd.read_csv(population_path)


population_query_engine = PandasQueryEngine(
    df=population_df,
    instruction_str=instruction_str,
    verbose=True,
    llm=llm,
)

population_query_engine.update_prompts({"pandas_prompt": new_prompt})


tools = [
    note_engine,
    QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="population_data",
            description="this gives information at the world population and demographics",
        ),
    ),
    QueryEngineTool(
        query_engine=note_engine,
        metadata=ToolMetadata(
            name="india_data",
            description="this gives detailed information about india the country",
        ),
    ),
]

agent = ReActAgent.from_tools(
    tools=tools,
    llm=llm,
    verbose=True,
    context = context
)  

while (prompt := input("Enter a prompt (e to exit): ")) != "e":
    result = agent.query(prompt)
    print(result)