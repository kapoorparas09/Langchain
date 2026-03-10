from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

llm = OllamaLLM(model="llama3.2")

parser = JsonOutputParser()

template1 = PromptTemplate(
    template="Give me the name, age and city of a fictional person :\n{format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

# Chain for the complete process
chain = template1 | llm | parser 

result = chain.invoke({})

print(result)