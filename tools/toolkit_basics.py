from langchain_core.tools import tool

@tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers a and b."""
    return a * b

@tool
def add(a: float, b: float) -> float:
    """Adds two numbers a and b."""
    return a + b

class MathToolkit:
    def gettools(self):
        return [multiply, add]
    

math_tools = MathToolkit()

tools= math_tools.gettools()

for tool in tools:
    print(f"Tool Name: {tool.name}")
    print(f"Description: {tool.description}")
    print(f"Arguments: {tool.args}")
    print(f"LLM View: {tool.args_schema.model_json_schema()}")
    print("\n")

