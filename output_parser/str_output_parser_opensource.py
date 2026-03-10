# from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2")

template1 = PromptTemplate(
    template="Generate a detailed report on the following topic:\n{topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Generate a short summary of the following text:\n{text}",
    input_variables=["text"]
)

prompt1 = template1.invoke({"topic": "Artificial Intelligence"})
result = llm.invoke(prompt1)

prompt2 = template2.invoke({"text": result})
summary = llm.invoke(prompt2)

print(summary)