from langchain_community.document_loaders import WebBaseLoader, TextLoader
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = OllamaLLM(model="llama3.2")

parser = StrOutputParser()

prompt = PromptTemplate(
    template = "give me the answer of the questions {question} based on the text {text} : \n {text}",
    input_variables=["question", "text"]
)

url = 'https://www.vijaysales.com/p/P232288/232286/apple-iphone-16-128gb-storage-white?utm_source=google&utm_medium=cpc&utm_campaign=pt-google-vijaysales-apple-pmax-purchase-shopping-iphone-16-na-in-all-13-09-2024&gad_source=1&gad_campaignid=21700908950&gbraid=0AAAAADLKtlkNePM6EVidpzoIVQJXXPpeA&gclid=CjwKCAjwyMnNBhBNEiwA-Kcgu_p8JDz5UlJVLZbsmELym2mfnj42VtL_A-EBtFh-Iguz7uXx5w_E8xoCXkUQAvD_BwE'

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | llm | parser

result = chain.invoke({'question': "What is this product about", "text": docs[0].page_content})

print(result)