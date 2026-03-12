from langchain_experimental.text_splitter import SemanticChunker
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

text_splitter = SemanticChunker(
    embeddings, 
    breakpoint_threshold_type="standard_deviation", # Fixed spelling
    breakpoint_threshold_amount=0.001
)

text = """Artificial intelligence (AI) is a branch of computer science.India win this worlcup. War is going on."""
chunks = text_splitter.create_documents([text])

print(len(chunks))
print(chunks)
