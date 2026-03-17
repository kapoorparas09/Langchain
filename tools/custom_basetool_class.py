# from langchain_core.tools import BaseTool
# from pydantic import BaseModel, Field
# from typing import Type

# class MultiplyClass(BaseModel):
#     a: float = Field(required= True, description="The first number to multiply")
#     b: float = Field(required= True, description="The second number to multiply")

# class MultiplyTool(BaseTool):
#     name = "multiply"
#     description = "Multiplies two numbers a and b."
#     args_schema: Type[BaseModel] = MultiplyClass

#     def _run(self, a: float, b: float) -> float:
#         return a * b        
    
# multiply_tool = MultiplyTool()

# result = multiply_tool.invoke({'a': 3, 'b': 4})
# print(result)
# print(multiply_tool.name)
# print(multiply_tool.description)


from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class MultiplyClass(BaseModel):
    # Removed 'required=True' as it's default and causes warnings
    a: float = Field(description="The first number to multiply")
    b: float = Field(description="The second number to multiply")

class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiplies two numbers a and b."
    args_schema: Type[BaseModel] = MultiplyClass

    def _run(self, a: float, b: float) -> float:
        return a * b        
    
multiply_tool = MultiplyTool()

result = multiply_tool.invoke({'a': 3, 'b': 4})
print(f"Result: {result}")
print(f"Tool Name: {multiply_tool.name}")