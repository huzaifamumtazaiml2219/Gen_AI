# Gen AI

Gen AI is a personal practice repository for learning and experimenting with Generative AI using LangChain. It contains examples and a small FastAPI chatbot demonstrating chat models (OpenAI & HuggingFace), persona modes, text embeddings, and structured output parsing. This repository documents a hands-on journey toward becoming a Gen AI engineer.

Repository: https://github.com/huzaifamumtazaiml2219/Gen_AI
Primary language: Python (100%)

## Table of contents

- [Highlights](#highlights)
- [Features](#features)
- [Quickstart](#quickstart)
  - [Requirements](#requirements)
  - [Install](#install)
  - [Environment variables](#environment-variables)
  - [Run the FastAPI chatbot](#run-the-fastapi-chatbot)
- [Project layout (example)](#project-layout-example)
- [Usage notes](#usage-notes)
  - [Persona modes](#persona-modes)
  - [Models & embeddings](#models--embeddings)
  - [Structured output parsing](#structured-output-parsing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Highlights

- Hands-on examples using LangChain to wire prompts, model calls, and retrieval.
- FastAPI chatbot with configurable persona modes (system prompts) to change behavior.
- Demonstrations of text embeddings for semantic search and retrieval-augmented generation.
- Examples of structured output parsing (validate/parse model responses against JSON schemas or dataclasses).

## Features

- Integrations: OpenAI and HuggingFace model examples
- FastAPI service exposing a chatbot API and interactive docs
- Persona-based behaviors (swap system prompts for different roles)
- Embeddings pipelines for semantic search and retrieval
- Sample notebooks / scripts for experimentation (add as you go)

## Quickstart

### Requirements

- Python 3.10+
- Git
- (Optional) virtualenv or conda

### Install

1. Clone the repository

   git clone https://github.com/huzaifamumtazaiml2219/Gen_AI.git
   cd Gen_AI

2. Create and activate a virtual environment

   python -m venv .venv
   source .venv/bin/activate    # macOS / Linux
   .venv\Scripts\activate     # Windows (PowerShell)

3. Install dependencies (if requirements.txt exists)

   pip install -r requirements.txt

### Environment variables

Create a `.env` file or export environment variables. Common variables used in examples:

- OPENAI_API_KEY — API key for OpenAI (if using OpenAI)
- HF_API_TOKEN — HuggingFace API token (if using HuggingFace)
- DATABASE_URL — optional, if persistence is used

### Run the FastAPI chatbot

Start the app during development with uvicorn (example path, adjust to actual app module):

   uvicorn app.main:app --reload

Then open the interactive docs at http://127.0.0.1:8000/docs to explore the endpoints.

## Project layout (example)

The repository is organized to support experimentation. Example layout:

- app/               # FastAPI application and API routes
- experiments/       # Notebooks and demo scripts
- langchain_configs/ # Prompt templates, persona configs, schema parsers
- embeddings/        # Embedding utilities and example data
- tests/             # Tests (if added)

Adjust this layout to match the actual project structure in the repo.

## Usage notes

### Persona modes

Persona modes are implemented as interchangeable system prompts or persona configs. Typical personas you might see or add:
- assistant — default helpful assistant
- tutor — teaching and explanatory style
- analyst — concise, factual, and analytical

Switch persona by passing a persona identifier to the API or by changing the persona configuration in code.

### Models & embeddings

- Chat model backends: OpenAI GPT-series, HuggingFace models (inference API or local)
- Embeddings: used for semantic retrieval, clustering, or similarity search

Model selection and provider configuration are handled in the project config; add or swap providers as needed.

### Structured output parsing

This project demonstrates how to constrain model outputs into structured data (JSON schema, Pydantic models, or dataclasses) for reliable downstream consumption. Use schema-first prompt design and parsing/validation helpers.

## Contributing

This is a personal practice project — contributions, issues, and suggestions are welcome. If you want to contribute:

1. Fork the repo
2. Create a feature branch
3. Open a pull request with a description of changes

Please add tests and update docs when adding features.

## License

No license file is included by default. Add a LICENSE file to explicitly set reuse terms.

## Contact

Owner: huzaifamumtazaiml2219
Repository: https://github.com/huzaifamumtazaiml2219/Gen_AI

Happy experimenting — welcome to the journey into Generative AI engineering!