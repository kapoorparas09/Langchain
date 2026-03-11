from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = OllamaLLM(model="llama3.2")

prompt_1 = PromptTemplate(
    template="Generate a detailed report on the following topic:\n{topic}",
    input_variables=["topic"]
)

prompt_2 = PromptTemplate(
    template = "Generate a 5 pointer summary of the following text:\n{text}",
    input_variables=["text"]
)

parser = StrOutputParser()

# Chain for the complete process: Generate report -> Parse output
chain = prompt_1 | llm | parser | prompt_2 | llm | parser

result = chain.invoke({"topic": "Artificial Intelligence"})

print(result)

# To visualize the chain graph uncomment the following line
# chain.get_graph().print_ascii()