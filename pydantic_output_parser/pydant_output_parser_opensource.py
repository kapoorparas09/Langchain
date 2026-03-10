from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

llm = OllamaLLM(model="llama3.2")

class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(gt= 18, description="The person's age")
    city: str = Field(description="The city where the person lives")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Give me the name, age and city of a fictional {place} person :\n" \
    "{format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt = template.invoke({"place": "indian"})

result = llm.invoke(prompt)

final_result = parser.parse(result)

print(final_result)