from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

pdf_loader = PyPDFLoader("DSA_Problems.pdf")

docs = pdf_loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100, 
    chunk_overlap=0,
    separator=''
    )

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

chunks = splitter.split_documents(docs)

print(chunks)