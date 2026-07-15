"""
Hello World Chain — LangChain
Chain: prompt -> LLM -> output parser
Requires: pip install langchain langchain-anthropic
Set your API key first: export ANTHROPIC_API_KEY="your-key-here"
"""

from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Prompt template
prompt = ChatPromptTemplate.from_template("Summarize the topic '{topic}' in exactly one line.")

# 2. LLM wrapper
llm = ChatAnthropic(model="claude-sonnet-4-6")

# 3. Output parser (raw text out)
output_parser = StrOutputParser()

# Chain = prompt -> LLM -> output parser
chain = prompt | llm | output_parser

if __name__ == "__main__":
    result = chain.invoke({"topic": "SIEM pipelines"})
    print(result)

    # Expected style of output:
    # "SIEM pipelines collect, normalize, correlate, and alert on
    #  security logs so analysts can catch threats in real time."
