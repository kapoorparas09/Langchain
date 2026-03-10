from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = OllamaLLM(model="llama3.2")

template1 = PromptTemplate(
    template="Generate a detailed report on the following topic:\n{topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Generate a short summary of the following text:\n{text}",
    input_variables=["text"]
)

parser = StrOutputParser()

# Chain for the complete process: Generate report -> Parse output -> Generate summary -> Parse output
chain = template1 | llm | parser | template2 | llm | parser

result = chain.invoke({"topic": "Artificial Intelligence"})

print(result)