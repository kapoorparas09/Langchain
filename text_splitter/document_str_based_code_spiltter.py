from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

splitter = RecursiveCharacterTextSplitter.from_language(
    language= Language.PYTHON,
    chunk_size=80, 
    chunk_overlap=0
)


text = """
class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(gt= 18, description="The person's age")
    city: str = Field(description="The city where the person lives")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Give me the name, age and city of a fictional person :\n" 
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
"""


chunk = splitter.split_text(text)

print(chunk)