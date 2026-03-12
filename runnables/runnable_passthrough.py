from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough


llm = OllamaLLM(model="llama3.2")

prompt_1 = PromptTemplate(
    template = "Tell me a joke on the topic : \n {topic}",
    input_variables=["topic"]
)

prompt_2 = PromptTemplate(
    template = "Explain the following joke : \n {joke}",
    input_variables=["joke"]
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt_1 , llm , parser)

parallel_chain = RunnableParallel({
    "joke" : RunnablePassthrough(),
    "explanation" : RunnableSequence(prompt_2 , llm , parser)
})

final_chain = RunnableSequence(joke_gen_chain , parallel_chain)

result = final_chain.invoke({"topic": "programming"})

print(result)