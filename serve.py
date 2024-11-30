from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes
import uvicorn


load_dotenv()

llm = ChatOpenAI(temperature=0.1, model="gpt-4")



system_prompt= "translate the following into {language}"
prompt_template= ChatPromptTemplate.from_messages([
    ("system", system_prompt), ("user", "{text}")
])

parser = StrOutputParser()

chaın =prompt_template | llm | parser

app = FastAPI()
add_routes(
    app,
    chaın,
    path="/chain"
)

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
