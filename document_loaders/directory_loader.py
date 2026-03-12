from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path = 'books',
    glob = '*.pdf',
    loader_cls = PyPDFLoader
)

docs = loader.load()

print(len(docs))

print(docs[10].page_content)
print(docs[10].metadata)