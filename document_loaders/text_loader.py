from langchain_ollama import OllamaLLM
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = OllamaLLM(model="llama3.2")

docs_loader = TextLoader("cricket.txt", encoding = 'utf-8')

docs = docs_loader.load()

prompt = PromptTemplate(
    template = "Summarize the following text : \n {text}",
    input_variables=["text"]
)

# print(docs)

print(docs[0].page_content)
print(docs[0].metadata)

parser = StrOutputParser()

chain = prompt | llm | parser

print(chain.invoke({"text": docs[0].page_content}))
