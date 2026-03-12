from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda


llm = OllamaLLM(model="llama3.2")

prompt = PromptTemplate(
    template = "Tell me a joke on the topic : \n {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

def word_count(text: str) -> int:
    return len(text.split())

joke_get_chain = RunnableSequence(prompt , llm , parser)

paraller_chain = RunnableParallel({
    "joke" : RunnablePassthrough(),
    "word_count" : RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_get_chain , paraller_chain)

result = final_chain.invoke({"topic": "programming"})

final_result = """ {} \n word count - {}""".format(result["joke"], result["word_count"])

print(final_result)