from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

embeddings = OllamaEmbeddings(model="nomic-embed-text")

doc_1 = Document(page_content="RCB is the winner of TATA IPL 2025 under the captancy of Virat Kohli. Virat Kohli is one of the gratest player of all the time ",
        metadata = {'team':"RCB"}
)
doc_2 = Document(page_content="MI is the winner of TATA IPL 2024 under the captancy of Rohit Sharma. Rohit Sharma is one of the gratest player of all the time ",
        metadata = {'team':"MI"}
)
doc_3 = Document(page_content="CSK is the winner of TATA IPL 2023 under the captancy of MS Dhoni. MS Dhoni is one of the gratest player of all the time ",
        metadata = {'team':"CSK"}
)   
doc_4 = Document(page_content="GT is the winner of TATA IPL 2022 under the captancy of Hardik Pandya. Hardik Pandya is one of the gratest player of all the time ",
        metadata = {'team':"GT"}
)

docs = [doc_1, doc_2, doc_3, doc_4]

# vector_store = Chroma(
#     embeddings,
#     persist_directory = 'chroma_db',
#     collection_name = 'sample'
# )

vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./chroma_db",
    collection_name="sample"
)

# result = vector_store.add_documents(docs)
# print(result)


# details = vector_store.get(include=['embeddings','documents','metadatas'])
# print(details)


# Similarity Search based on score and without score question answering.
depth_details = vector_store.similarity_search("Which team won the TATA IPL 2025?", k=2)

depth_details_score = vector_store.similarity_search_with_score("Which team won the TATA IPL 2025?", k=2)   

# print(depth_details)
# print(depth_details_score)


# Update Document
update_docs_1 = Document(page_content="RCB is the winner of TATA IPL 2025 under the captancy of Virat Kohli. Virat Kohli is one of the gratest player of all the time. Virat Kohli is very strict about this diet and workout plans. ",
        metadata = {'team':"RCB"}
)

docs_update = vector_store.update_document(document_id = 'ea9479d0-5c94-44ca-842a-29523c1ac8d1', document = update_docs_1)

updated_details = vector_store.get(include=['embeddings','documents','metadatas'])
# print(updated_details)



#  Delete Document
delete_doc = vector_store.delete(ids = ['68c9175a-7862-47a0-8774-f5fbcda4e514'])

doc_deleted = vector_store.get(include=['embeddings','documents','metadatas'])
# print(doc_deleted)

