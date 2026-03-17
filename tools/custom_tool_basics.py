from langchain_core.tools import tool

# Creating a simple multiplication tool

#  Simple multiplication function
# def multiply(a,b):
#     """Multiplies two numbers a and b."""
#     return a * b


#  Add type hints to the function
# def multiply(a: float, b: float) -> float:
#     """Multiplies two numbers a and b."""
#     return a * b


#  Converting this multiply function into a tool

@tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers a and b."""
    return a * b


#  Using the tool

result = multiply.invoke({'a': 3, 'b': 4})
print(result)


#  get details of the tool

print(multiply.name)
print(multiply.description)
print(multiply.args)

# LLM view on the tool

print(multiply.args_schema.model_json_schema())