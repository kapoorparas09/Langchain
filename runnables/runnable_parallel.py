from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

llm = OllamaLLM(model="llama3.2")

prompt_1 = PromptTemplate(
    template = "Generate a tweet about the topic : \n {topic}",
    input_variables=["topic"]
)

prompt_2 = PromptTemplate(
    template = "Generate a Linkedin post about the topic  : \n {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "tweet" : RunnableSequence(prompt_1 , llm , parser),
        "linkedin_post" : RunnableSequence(prompt_2 , llm , parser)
    }
)

result = parallel_chain.invoke({"topic": "Artificial Intelligence"})

print(result)