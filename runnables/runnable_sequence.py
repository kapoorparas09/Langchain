from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence


llm = OllamaLLM(model="llama3.2")

prompt_1 = PromptTemplate(
    template = "Tell me a joke on the topic : \n {topic}",
    input_variables=["topic"]
)

prompt_2 = PromptTemplate(
    template = "Explain the following joke : \n {joke}",
    input_variables=["joke"]
)

parser = StrOutputParser()

chain = RunnableSequence(prompt_1 , llm , parser, prompt_2 , llm , parser)

print(chain.invoke({"topic": "programming"}))