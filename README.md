<p align="center">
  <a href="https://apac.ai"><img src="/data-ocean-banner.png" alt="Ocean logo"></a>
</p>

<p align="center">
    <b>Ocean - Ultra-Fast MultiModality Vector Database</b>. <br />
    Embed anything: images, pdfs, videos, movies and retrieve them back at lightspeed
</p>

<p align="center">
  <a href="https://discord.gg/MMeYNTmh3x" target="_blank">
      <img src="https://img.shields.io/discord/1073293645303795742" alt="Discord">
  </a> |
  <a href="https://github.com/ocean-core/ocean/blob/master/LICENSE" target="_blank">
      <img src="https://img.shields.io/static/v1?label=license&message=Apache 2.0&color=white" alt="License">
  </a> |
  <a href="https://docs.tryocean.com/" target="_blank">
      Docs
  </a> |
  <a href="https://www.tryocean.com/" target="_blank">
      Homepage
  </a>
</p>

<p align="center">
  <a href="https://github.com/ocean-core/ocean/actions/workflows/ocean-integration-test.yml" target="_blank">
    <img src="https://github.com/ocean-core/ocean/actions/workflows/ocean-integration-test.yml/badge.svg?branch=main" alt="Integration Tests">
  </a> |
  <a href="https://github.com/ocean-core/ocean/actions/workflows/ocean-test.yml" target="_blank">
    <img src="https://github.com/ocean-core/ocean/actions/workflows/ocean-test.yml/badge.svg?branch=main" alt="Tests">
  </a>
</p>

```bash
pip install oceandb # python client
# for javascript, npm install oceandb!
# for client-server mode, docker-compose up -d --build
```

The core API is only 4 functions (run our [💡 Google Colab](https://colab.research.google.com/drive/1QEzFyqnoFxq7LUGyP1vzR4iLt9PpCDXv?usp=sharing) or [Replit template](https://replit.com/@swyx/BasicOceanStarter?v=1)):

```python
import oceandb
from oceandb import emedding_functions

# setup Ocean in-memory, for easy prototyping. Can add persistence easily!
client = oceandb.Client()

# Create collection. get_collection, get_or_create_collection, delete_collection also available!
collection = client.create_collection("all-my-documents")

# Add docs to the collection. Can also update and delete. Row-based API coming soon!
collection.add(
    documents=["This is document1", "This is document2"], # we handle tokenization, embedding, and indexing automatically. You can skip that and add your own embeddings as well
    metadatas=[{"source": "notion"}, {"source": "google-docs"}], # filter on these!
    ids=["doc1", "doc2"], # unique for each doc
)

#for example to use imagebindfunction
text_embedding_function = embedding_functions.ImageBindEmbeddingFunction(modality=ModalityType.TEXT)
vision_embedding_function = embedding_functions.ImageBindEmbeddingFunction(modality=ModalityType.VISION)
audio_embedding_function = embedding_functions.ImageBindEmbeddingFunction(modality=ModalityType.AUDIO)


# Query/search 2 most similar results. You can also .get by id
results = collection.query(
    query_texts=["This is a query document"],
    n_results=2,
    # where={"metadata_field": "is_equal_to_this"}, # optional filter
    # where_document={"$contains":"search_string"}  # optional filter
)
```

## Features

- **Simple**: Fully-typed, fully-tested, fully-documented == happiness
- **Integrations**: [`🦜️🔗 LangChain`](https://blog.langchain.dev/langchain-ocean/) (python and js), [`🦙 LlamaIndex`](https://twitter.com/atroyn/status/1628557389762007040) and more soon
- **Dev, Test, Prod**: the same API that runs in your python notebook, scales to your cluster
- **Feature-rich**: Queries, filtering, density estimation and more
- **Free & Open Source**: Apache 2.0 Licensed

## Use case: ChatGPT for **\_\_**

For example, the `"Chat your data"` use case:

1. Add documents to your database. You can pass in your own embeddings, embedding function, or let Ocean embed them for you.
2. Query relevant documents with natural language.
3. Compose documents into the context window of an LLM like `GPT3` for additional summarization or analysis.

## Embeddings?

What are embeddings?

- [Read the guide from OpenAI](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)
- **Literal**: Embedding something turns it from image/text/audio into a list of numbers. 🖼️ or 📄 => `[1.2, 2.1, ....]`. This process makes documents "understandable" to a machine learning model.
- **By analogy**: An embedding represents the essence of a document. This enables documents and queries with the same essence to be "near" each other and therefore easy to find.
- **Technical**: An embedding is the latent-space position of a document at a layer of a deep neural network. For models trained specifically to embed data, this is the last layer.
- **A small example**: If you search your photos for "famous bridge in San Francisco". By embedding this query and comparing it to the embeddings of your photos and their metadata - it should return photos of the Golden Gate Bridge.

Embeddings databases (also known as **vector databases**) store embeddings and allow you to search by nearest neighbors rather than by substrings like a traditional database. By default, Ocean uses [ImageBind](https://github.com/facebookresearch/ImageBind) to embed for you but you can also use OpenAI embeddings, Cohere (multilingual) embeddings, or your own.

## Get involved at Agora

Ocean is a rapidly developing project. We welcome PR contributors and ideas for how to improve the project.

- [Join the conversation on Discord](https://discord.gg/sbYvXgqc)
- [Review the roadmap and contribute your ideas](https://docs.tryocean.com/roadmap)
- [Grab an issue and open a PR](https://github.com/ocean-core/ocean/issues)

## License

[Apache 2.0](./LICENSE)
