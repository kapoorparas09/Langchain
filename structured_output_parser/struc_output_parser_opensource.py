from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers.structured import ResponseSchema, StructuredOutputParser

llm = OllamaLLM(model="llama3.2")

schema = [
    ResponseSchema(name = "fact_1", description = "Fact 1 about the topic"),
    ResponseSchema(name = "fact_2", description = "Fact 2 about the topic"),
    ResponseSchema(name = "fact_3", description = "Fact 3 about the topic"),
    ResponseSchema(name = "fact_4", description = "Fact 4 about the topic"),
    ResponseSchema(name = "fact_5", description = "Fact 5 about the topic"),

]

parser = StructuredOutputParser.from_response_schemas(schema)

template  = PromptTemplate(
    template="List 5 interesting facts about the following topic:\n{topic}\n\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt = template.invoke({"topic": "Artificial Intelligence"})

result = llm.invoke(prompt)
final_result = parser.parse(result)
print(final_result)

