from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

llm = OllamaLLM(model="llama3.2")

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age and city of a fictional person :\n{format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

prompt = template.format()

result = llm.invoke(prompt)

final_result = parser.parse(result)

print(final_result)