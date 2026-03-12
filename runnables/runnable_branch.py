from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch


llm = OllamaLLM(model="llama3.2")

prompt_1= PromptTemplate(
    template = "Write a detailed report on topic : \n {topic}",
    input_variables=["topic"]
)

prompt_2 = PromptTemplate(
    template = "Summarize the following text : \n {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt_1 , llm , parser)

branch_chain = RunnableBranch(
    (lambda x:len(x.split())>150, RunnableSequence(prompt_2 , llm , parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain , branch_chain)

result = final_chain.invoke({"topic": "Russia VS Ukraine"})

print(result)