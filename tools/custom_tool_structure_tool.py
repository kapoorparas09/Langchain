from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

class MultiplyClass(BaseModel):
    a: float = Field(required= True, description="The first number to multiply")
    b: float = Field(required= True, description="The second number to multiply")

def multiply(a: float, b: float) -> float:
    """Multiplies two numbers a and b."""
    return a * b

multiply_tool = StructuredTool.from_function(
    func=multiply,
    name="multiply",
    description="Multiplies two numbers a and b.",
    args_schema=MultiplyClass
)

result = multiply_tool.invoke({'a': 3, 'b': 4})
print(result)
print(multiply_tool.name)
print(multiply_tool.description)