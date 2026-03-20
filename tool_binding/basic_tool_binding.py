from langchain_core.tools import tool
from langchain_ollama import OllamaLLM
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

# llm = OllamaLLM(model="llama3.2")
llm = ChatOllama(model="llama3.2")

#  Tool creation
@tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers a and b."""
    return a * b

#  Tool Binding

llm_with_tool = llm.bind_tools([multiply])

llm_with_tool.invoke('Hi how are you!')

query = HumanMessage("Can you multiply 8 with 7!")

messages = [query]

# print(messages)

result = llm_with_tool.invoke(messages)

messages.append(result)

# print(result.tool_calls[0])

# Tool execution result

final_result = multiply.invoke(result.tool_calls[0])

messages.append(final_result)

# print(messages)


final_output = llm_with_tool.invoke(messages).content

print(final_output)

