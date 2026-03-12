from langchain_ollama import OllamaLLM
from langchain_community.document_loaders import PyPDFLoader


llm = OllamaLLM(model="llama3.2")

pdf_loader = PyPDFLoader("DSA_Problems.pdf")

docs = pdf_loader.load()

print(len(docs))

print(docs[1].page_content)
print(docs[1].metadata)