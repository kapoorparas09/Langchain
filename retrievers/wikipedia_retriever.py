from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=2 , lang = 'en')

query = 'India–Pakistan relations'

docs = retriever.invoke(query)

for i , docs in enumerate(docs):
    print(f"Document {i+1} : \n")
    print(docs.page_content)
    print("\n\n")   