# Langchain
This repository consits of the basic content and knowledge regarding the Langchain.


## String Output parser -> When we need string as the output from the LLM.
## Json Output parser -> Used when we need json as the output from the LLM (Not Schema enforced).
## Structured Output parser -> Schema enforced , we can predefine the schema (No Data validation).
## Pydantic Output parser -> Gives structured output and also so Data Validation.

## Move to output_parser directory to check how the parser works

- str_output_parser_opensource file consists of simple rules of providing the outputs using multiple templates.
- str_output_parser_opensource_2 file consists of the string output parser , with the help of that we can easily build the chain that works on the multiple templates.

## Move to json_output_parser directory to check how the parser works

- json_output_parser_opensource file consists of simple rules of providing the outputs.
- json_output_parser_opensource_chain file consists of the json output parser , with the help of that we can easily build the chain.

- Json output parser is not schema enforced .i.e. here we can not decide the schema LLM model itself will define the schema of json we can not change that as per our requirements.


## Move to structured_output_parser directory to check how the parser works

- structured_output_parser_opensource file consists of simple rules of providing the outputs.
- structured_output_parser_opensource_chain file consists of the structured output parser , with the help of that we can easily build the chain.

- structured output parser is the parser in which we can define our schema or can say a predefined schema.

- Using Structured output parser we can not do **Data Validation**, like if we need to fetch specific details like name, age or city we will not be able to fetch that information.

## Pydantic output parser

- Pydantic_output_parser_opensource file consists of simple rules of providing the outputs.
- Pydantic_output_parser_opensource_chain file consists of the Pydantic output parser , with the help of that we can easily build the chain.

- Pydantic output parser is the parser in which we can define our schema or can say a predefined schema.

- Using Pydantic output parser we can  do **Data Validation**, like if we need to fetch specific details like name, age or city we will be able to fetch that information.


# Chains

With the help of chains we can create pipelines for the complete process rather than manual method. With the help of chains we can automate the process.

#### Types of chains:-

- Simple chain
- Sequential chain
- Parallel chain
- Conditional chain

**chains** directory consists of different types of chains and their implementaions using opensource LLM.

NOTE:- This repository consists of the Langchain content based on the opensource model. Some code may consists of close source models but most of the topics are covered using opensource models


# Author

Paras Kapoor

AI Research Engineer
Specializing in **Generative AI, Computer Vision, Deep Learning, and Production ML Systems**

---
