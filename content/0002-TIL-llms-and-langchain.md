Title: TIL: How LangChain makes it easy to interact with LLMs
Date: 2023-09-17
Category: TIL
Slug: til-how-langchains-interact-with-llms
Modified: 2023-09-17
Tags: langchain, python, generative-ai, llm
Authors: Saqibur Rahman
Summary: A quick look at what I learned when adopting an LLM use-case at a work project


## A summary of my studies
- `LangChain` provides a "sensible" framework that does a lot of heavy lifting for
us - [LangChain: Build AI apps with LLMs through composability](https://news.ycombinator.com/item?id=34422627)
- Seems like it's also a widely adopted (across different tech companies)
approach for the last few months at least
- Two main advantages backend devs, it can directly integrate;
    - with your database with a [SQLChain](https://python.langchain.com/docs/use_cases/qa_structured/sql)
    - with your API with an [APIChain](https://python.langchain.com/docs/use_cases/apis). It's easy
    enough that if you provide it with a standard OpenAPI schema, it's able to
    understand which API to call and fetch data from to answer the question
- You can think of it like writing a step-by-step, repeatable flow for interacting
  with an LLM in a very iteration friendly way (you can build on your prompts
  and templates quite easily) - that is, composing a bunch of different
  prompts/instructions and chaining them together into a desirable outcome. What
  it does boil down to, at a super high-level, is a
  [DAG](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html)
- One thing to note, it's not restricted to OpenAI, but rather can be tweaked to
work with other models as well - for instance, open source models available on
hugging face.


## Counter-points
`LangChain` is essentially an abstraction over how you'd normally query LLMs -
so while it doesn't do anything fancy (and in rare cases, cannot be used for
super customised integrations), it does get the job done in most
application-specific use cases. Some rants on Hacker News on why it "sucks":

- [The problem with LangChain](https://news.ycombinator.com/item?id=36725982)
- [LangChain is pointless](https://news.ycombinator.com/item?id=36645575)


<!-- ## Examples (via screenshots): TODO.
- The first screenshot shows what I got after asking my "API" about "myself"
- The second shows what I got when asking about "me" and the APIChain correctly hits the me API that I have
- The third screenshot shows what I got when asking about my phone number
- Just a general question about the missions we have in the system -->



### Case:
- [Klarna](https://www.klarna.com/international/press/klarna-brings-smoooth-shopping-to-chatgpt/)
has a nice documentation and implementation of this (LangChain refers to this in their docs)


###### References:
- [Intro to LangChain](https://python.langchain.com/docs/get_started/introduction)
- [Interacting with APIs](https://python.langchain.com/docs/use_cases/apis)
