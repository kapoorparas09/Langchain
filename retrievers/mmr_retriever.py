from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

embeddings = OllamaEmbeddings(model="nomic-embed-text")

doc_1 = Document(page_content="RCB is the winner of TATA IPL 2025 under the captancy of Virat Kohli. Virat Kohli is one of the gratest player of all the time "
)
doc_2 = Document(page_content="RCB is the winner of TATA IPL 2025 under the captancy of Virat Kohli. "
)
doc_3 = Document(page_content="CSK is the winner of TATA IPL 2023 under the captancy of MS Dhoni. MS Dhoni is one of the gratest player of all the time "
)   
doc_4 = Document(page_content="GT is the winner of TATA IPL 2022 under the captancy of Hardik Pandya. Hardik Pandya is one of the gratest player of all the time "
)

docs = [doc_1, doc_2, doc_3, doc_4]

vector_store = FAISS.from_documents(
    documents=docs,
    embedding=embeddings,
)


retriever = vector_store.as_retriever(
    search_type='mmr',
    search_kwargs={"k":2, "lambda_mult":1}
)

query = "Which team won the TATA IPL 2025?"
docs = retriever.invoke(query)
for i , docs in enumerate(docs):
    print(f"Document {i+1} : \n")
    print(docs.page_content)
    print("\n\n")