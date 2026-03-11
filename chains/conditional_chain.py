from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from typing import Literal

llm = OllamaLLM(model="llama3.2")

parser = StrOutputParser()


class FeedbackSentiment(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the feedback")

parser_2 = PydanticOutputParser(pydantic_object=FeedbackSentiment)

prompt_1 = PromptTemplate(
    template="""Analyze the sentiment of this feedback.
Return ONLY a JSON object. Do NOT include any introductory text or explanations.

Feedback: {feedback}

{format_instruction}""",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser_2.get_format_instructions()}
)

prompt_2 = PromptTemplate(
    template = "Write one appropriate response for this positive feedback:\n{feedback}",
    input_variables=["feedback"]
)

prompt_3 = PromptTemplate(
    template = "Write one appropriate response for this negative feedback:\n{feedback}",
    input_variables=["feedback"]
)

classifier_chain = prompt_1 | llm | parser_2

branch_chain =  RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt_2 | llm | parser),
    (lambda x: x.sentiment == "negative", prompt_3 | llm | parser),
    RunnableLambda(lambda x: "No sentiment extracted.")

)

chain = classifier_chain | branch_chain

result = chain.invoke({"feedback": "The product is really terrible and I hate it!"})

print(result)   

# To visualize the chain graph uncomment the following line
# chain.get_graph().print_ascii()