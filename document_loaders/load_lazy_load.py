from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
    path = 'books',
    glob = '*.pdf',
    loader_cls = PyPDFLoader
)

# docs = loader.load()  # This will load all the pdf files inside the provided directory at once.

docs = loader.lazy_load()  # This will create a generator object which will load the pdf files one by one when we iterate over it.

for document in docs:
    print(document.metadata)