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

# Runnables

With the help of runnables we can use different types of runnables based on the type of process we are following.

## Types of Runnables:-

- Sequence
- Parallel
- Pass Through
- Lambda
- Branch

# Documents Loader

With the help of document loader we can load any type of document.
I have also defined some of the documents loaders.

## Types of Documents loaders:-

- Text loader
- pdf loader
- webbase loader
- directory loader
- csv loader


# Text Splitter

With the help of text splitter we can spilt the large textual data into smaller chunks.

## Types of Splitter

- Length based
- Text Structure based
- Document Structure based
- Semantic Meaning based.


# Vector Store

In vector store we can store data in form of vectors .i.e. we can save data in form of numbers. Where we can add docs, modify the docs, delete the document.
We can do the similarity serach to get the perfect results, we can do simple similarity serach or can do similarity search with score where we can get the score of the result like how much similar is the result to the query. Lower the similarity score better the result (~0).

# Retrievers

Retriever are used to retrive the content for the relevent query.

## Types of Retrivers

- Wikipedia retriever
- Vector store retriever
- Maximal Marginal Relevance (MMR)
- Multi Query retriever
- Contextual compression retriever

# Tools 

Tools are used in langchain so that we can use some methods that an LLM can not perform or some methods that are only related to our dataset only.

## Types of Tools

- Built-in tools
- Custom tools
    - @tool (tool decorator)
    - Structure and pydantic tool
    - Base Tool

## Tool Binding 

- In tool binding we will use various types of techniques like tool creation, tool binding and tool execution and finally executing the tool with LLM.

NOTE:- This repository consists of the Langchain content based on the opensource model. Some code may consists of close source models but most of the topics are covered using opensource models

# Author

Paras Kapoor

AI Research Engineer
Specializing in **Generative AI, Computer Vision, Deep Learning, and Production ML Systems**

---
