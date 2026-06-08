#  GenAI & Agentic AI Learning Journey

This repository documents my intensive learning journey focused on **Generative AI, LangChain, and Agentic AI Systems**.

The objective is to build practical AI Engineering skills through hands-on implementation of modern AI frameworks, workflows, and applications.

---

#  Learning Goals

Build a strong foundation in:

* Large Language Models (LLMs)
* Prompt Engineering
* LangChain
* Prompt Engineering
* Embedding Models
* Output Parsing
* Structured Outputs
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Agentic AI
* LangGraph
* AI Agents and Workflows

---

#  Learning Roadmap

## Week 1: Generative AI with LangChain

### Topics

* Understanding LLMs
* Open Source vs Closed Source Models
* Chat Models
* Prompt Templates
* Chat Prompt Templates
* Message Roles
* Message Roles (System, Human, AI)
* Output Parsers
* Structured Outputs
* Chains
* LCEL (LangChain Expression Language)
* Embedding Models
* Vector Databases
* FAISS
* RAG Applications

---

## Week 2: Agentic AI with LangGraph

### Topics

* Agent Fundamentals
* Tool Calling
* Multi-Agent Systems
* LangGraph
* Agent Workflows
* Memory
* Human-in-the-Loop Systems
* End-to-End AI Applications

---

#  Daily Learning Log

| Day   | Topic                                    | Status |
| ----- | ---------------------------------------- | ------ |
| Day 1 | Chat Models & Embeddings                 | DONE      |
| Day 2 | Prompt Templates & Chat Prompt Templates | DONE      |
| Day 3 | Output Parsers & Structured Outputs      | DONE      |
| Day 4 | Chains & LCEL                            | PROGRESS     |
| Day 5 | Vector Databases (FAISS)                 | PENDING      |
| Day 6 | RAG Applications                         | PENDING      |
| Day 7 | Mini RAG Project                         | PENDING      |

---

#  Progress

---

# Day 1 — LLMs, Chat Models & Embeddings

## Learned

### LLM Fundamentals

* What Large Language Models (LLMs) are
* Open Source vs Closed Source Models
* Model Providers and APIs
* Local vs Cloud Inference

### Chat Models

Implemented:

* OpenAI Chat Models
* Anthropic Chat Models
* Google Gemini Chat Models
* Hugging Face Chat Models

### Embedding Models

Implemented:

* OpenAI Embeddings
* Hugging Face Embeddings
* Sentence Transformers

### Concepts Practiced

* Semantic Search
* Cosine Similarity
* Vector Embeddings
* Document Similarity

### Technologies Used

* Python
* LangChain
* Hugging Face
* OpenAI
* Google Gemini
* Sentence Transformers
* Scikit-Learn

---


# Day 2 — Prompt Templates

## Learned

### Prompt Engineering

* PromptTemplate
* ChatPromptTemplate
* Dynamic Variables
* Prompt Reusability
* Context Injection

### Message Roles

* System Messages
* Human Messages
* AI Messages

## Day 2

### LangChain Prompt Templates

Learned:

* Prompt Engineering Fundamentals
* PromptTemplate
* ChatPromptTemplate
* System Messages
* Human Messages
* AI Messages
* Dynamic Variable Injection
* Prompt Reusability
* Structured Prompt Design

### Implementations

* Single Variable Prompt Templates
* Multiple Variable Prompt Templates
* Chat Prompt Templates
* Prompt-Based Chatbot
* Streamlit Prompt UI
* System + Human Message Workflows
* Interactive Prompt UI using Streamlit
* Prompt-based Chatbot


### Concepts Practiced

* Prompt Formatting
* Dynamic Prompt Generation
* Role-Based Messaging
* Context Management
* Context Injection
* Role-Based Messaging
* Dynamic Prompt Generation
* Reusable Prompt Components

### Technologies Used

* Python
* LangChain
* Streamlit
* OpenAI
* Google Gemini

---

# Day 3 — Output Parsers & Structured Outputs

## Learned

### Output Parsers

Understanding how LLM responses can be converted into structured and reliable formats.

### Output Parsers Explored

#### StrOutputParser

Used for converting model responses into plain text strings.

Implemented:

* Prompt → Model → Parser Chains
* LCEL Pipelines
* Text Generation Workflows

#### StructuredOutputParser

Used for generating structured JSON outputs.

Implemented:

* ResponseSchema
* Format Instructions
* Structured JSON Responses

#### PydanticOutputParser

Used for validating LLM outputs using predefined schemas.

Implemented:

* Pydantic Models
* Structured Data Validation
* Field Extraction

#### TypedDict Structured Outputs

Implemented:

* TypedDict Schemas
* Type-Safe Responses
* Structured Output Validation

### Concepts Practiced

* Output Parsing
* Response Validation
* Structured Response Generation
* JSON Formatting
* Type-Safe LLM Outputs

### Technologies Used

* Python
* LangChain
* Pydantic
* TypedDict
* Hugging Face

---

# Day 4 — Chains & LCEL Runnables

## Learned

### Chains

Understanding how multiple LangChain components can be connected together to build complete AI workflows.

Implemented:

* Prompt → Model → Parser Chains
* Sequential Chains
* Chain Composition
* End-to-End LLM Pipelines

### LCEL (LangChain Expression Language)

Learned how LangChain uses LCEL to build modular and composable AI workflows.

Implemented:

#### RunnableSequence

Used for executing components sequentially.

Implemented:

* Prompt → Model → Parser Workflow
* Multi-Step Execution Pipelines

#### RunnableParallel

Used for executing multiple chains simultaneously.

Implemented:

* Parallel LLM Calls
* Multi-Output Generation
* Concurrent Workflow Execution

#### RunnablePassthrough

Used for passing original inputs alongside generated outputs.

Implemented:

* Input Preservation
* Context Passing
* Data Enrichment Pipelines

### Concepts Practiced

* Chain Composition
* Sequential Execution
* Parallel Execution
* LCEL Syntax
* Runnable Interfaces
* Pipeline Design
* Workflow Orchestration

### Technologies Used

* Python
* LangChain
* Hugging Face
* Pydantic
* LCEL

---

## Day 5 – Document Loaders

### Topics Covered

- Introduction to Document Loaders
- Loading text files using `TextLoader`
- Loading PDF documents using `PyPDFLoader`
- Loading web pages using `WebBaseLoader`
- Extracting content from different data sources
- Understanding the role of document loading in RAG pipelines

### Files Created

- `textloader.py`
- `pypdfloader.py`
- `webbaseloader.py`

### Key Learnings

- Learned how LangChain loads data from various sources into a standardized document format.
- Understood the difference between text, PDF, and web-based document loading.
- Explored document metadata and page content extraction.
- Built the foundation required for embeddings and retrieval systems.

### Outcome

Successfully loaded and processed documents from local files, PDFs, and websites using LangChain Document Loaders.

---

## Day 6 – Text Splitters

### Topics Covered

- Introduction to Text Splitting
- Why chunking is important for LLM applications
- `CharacterTextSplitter`
- `RecursiveCharacterTextSplitter`
- Chunk Size and Chunk Overlap
- Length-Based Text Splitting

### Files Created

- `lengthbased.py`

### Key Learnings

- Learned how large documents are divided into smaller chunks before generating embeddings.
- Understood the impact of chunk size and overlap on retrieval quality.
- Explored different text splitting strategies available in LangChain.
- Prepared documents for efficient storage in vector databases.

### Outcome

Successfully implemented text chunking techniques and understood their importance in Retrieval-Augmented Generation (RAG) systems.

---

#  Repository Structure

```text
LANGCHAIN/
│
├── langchainModel/
│   │
│   ├── 1.LLMs/
│   │   └── 1_llm_demo.py
│   │
│   ├── 2.ChatModels/
│   │   ├── 1_chatmodel_openai.py
│   │   ├── 2_chatmodel_anthropic.py
│   │   ├── 3_chatmodel_google.py
│   │   ├── 4_chatmodel_hf_api.py
│   │   └── 5_chatmodel_hf_local.py
│   │
│   ├── 3.EmbeddingModels/
│   │   ├── 1_embedding_openai_query.py
│   │   ├── 2_embedding_openai_docs.py
│   │   ├── 3_embedding_sentence_local.py
│   │   └── 4_document_similarity.py
│   │
│   ├── .env
│   └── requirements.txt
=======
* OpenAI / Gemini APIs
* Python Dotenv

---

# Repository Structure

```text
langchain/
├── langchainModel/
│   ├── 1.ChatModels/
│   └── 2.EmbeddingModels/
│
├── langchainPrompt/
│   ├── chatbot.py
│   ├── messages.py
│   ├── prompt_ui.py
│   ├── .env
│   └── requirements.txt
│
├── langchainOutputParser/
│   ├── stroutputparser.py
│   ├── stroutputparser1.py
│   ├── structureoutputparser.py
│   ├── jsonoutputparser.py
│   ├── pydanticoutputparser.py
│   ├── .env
│   └── requirements.txt
│
├── langchainStructureOutput/
│   ├── json_schema.json
│   ├── pydantic.py
│   ├── typedic_demo.py
│   ├── with_struct_json.py
│   ├── with_struct_pydantic.py
│   ├── with_struct_type_dic.py
│   ├── .env
│   └── requirements.txt
│
├── langchainChain/
│   │
│   ├── simple_chain.py
│   ├── sequential_chain.py
│   ├── parallel_chain.py
│   ├── runnableparallel.py
│   ├── runnablepassthrough.py
│   ├── runnablesequence.py
│   ├── conditional_chain.py
│   ├── aam-zindgi.py
│   ├── requirements.txt
│   ├── .env
│   └── venv/
|
├── textSplitter 
│   ├── lengthbased.py 
│   ├── requirements.txt 
|   └── venv/
|
├── documentLoader 
│   ├── cricket.txt 
│   ├── pypdfloader.py 
│   ├── textloader.py 
│   ├── webbaseloader.py 
│   ├── requirements.txt 
│   └── venv/
|
├── .gitignore
└── README.md
│   └── requirements.txt
│
├── README.md
└── requirements.txt

```

---


#  Current Status

Completed:

* LLM Fundamentals
* Chat Models
* Embedding Models
* Prompt Templates
* Chat Prompt Templates
* Message Roles
* Output Parsers
* Structured Outputs
* Chains
* LCEL (LangChain Expression Language)
* Document Loaders
* Text Splitters

Remaining

* Embedding Pipelines
* Vector Databases
* FAISS
* Vector Stores
* Retrieval-Augmented Generation (RAG)
* Mini RAG Project

---

#  Upcoming Topics

## Week 1 Remaining

* Vector Stores
* RAG Applications

## Week 2

* Agents
* Tool Calling
* LangGraph Fundamentals
* Multi-Agent Systems
* Memory
* Agent Workflows
* Human-in-the-Loop Systems
* End-to-End Agentic AI Applications

---

#  Technologies Used

* Python
* LangChain
* LangGraph
* Hugging Face
* OpenAI
* Anthropic
* Google Gemini
* Sentence Transformers
* Scikit-Learn
* Streamlit
* Pydantic
* TypedDict

---

#  End Goal

Build production-oriented AI Engineering skills through practical implementation of:

* LLM Applications
* Prompt Engineering
* Embedding Systems
* RAG Pipelines
* AI Agents
* LangGraph Workflows
* End-to-End AI Applications

This repository is updated continuously as new concepts, implementations, and projects are completed throughout the learning journey.

 Next Topic: vector  , retriever

---
