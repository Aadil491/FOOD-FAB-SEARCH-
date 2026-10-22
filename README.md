# FOOD-FAB-SEARCH

## 📌 Project Overview

The **AI-Powered Food Menu Assistant** is a Retrieval-Augmented Generation (RAG) application that answers natural language questions about food items available in a menu stored in JSON format.

The application uses **LangChain** to process user queries, **Google Gemini** to generate intelligent responses, **Hugging Face sentence embeddings** to represent menu data as vectors, and **ChromaDB** to retrieve relevant information.

Users can ask questions such as *"Give me a variety of Jain thali food"* and receive helpful answers based on the information available in the menu dataset.

## 🎯 Objectives

- Build an AI-powered question-answering system for food menus.
- Process and split structured JSON menu data into manageable chunks.
- Generate vector embeddings for semantic search.
- Retrieve relevant menu information based on user queries.
- Generate context-aware responses using Google Gemini.
- Provide accurate answers grounded in the supplied menu data.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | RAG pipeline and LLM integration |
| Google Gemini | Natural language response generation |
| Hugging Face | Text embedding generation |
| Sentence Transformers | Semantic representation of menu data |
| ChromaDB | Vector storage and similarity search |
| RecursiveJsonSplitter | Splitting structured JSON data |
| Google Colab | Development and execution environment |

## 🏗️ System Architecture

The application follows a Retrieval-Augmented Generation workflow:

1. **Input:** Load food menu data from a JSON file.
2. **JSON Processing:** Split the menu data into smaller chunks.
3. **Embedding Generation:** Convert the chunks into vector representations using a Hugging Face embedding model.
4. **Vector Storage:** Store the vectors in ChromaDB.
5. **Query Processing:** Accept a user's natural language question.
6. **Information Retrieval:** Retrieve the five most relevant chunks from the vector store.
7. **Answer Generation:** Pass the retrieved context and question to Google Gemini through LangChain.
8. **Output:** Display the generated answer in a readable Markdown format.

### Workflow

```text
Food Menu JSON
      |
      v
JSON Loading and Chunking
      |
      v
Hugging Face Embeddings
      |
      v
ChromaDB Vector Store
      |
      v
User Question
      |
      v
Semantic Retrieval (Top 5)
      |
      v
Google Gemini + LangChain
      |
      v
Context-Aware Answer
```

## 📂 Project Structure

```text
AI-Food-Menu-Assistant/
│
├── menu_incoming_json_log.json
├── food_menu_assistant.ipynb
├── requirements.txt
└── README.md
```

- `menu_incoming_json_log.json`: Contains the food menu data.
- `food_menu_assistant.ipynb`: Jupyter Notebook containing the implementation.
- `requirements.txt`: Lists the required Python dependencies.
- `README.md`: Project documentation.

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI-Food-Menu-Assistant
```

Alternatively, upload the notebook and JSON dataset directly to Google Colab.

### Step 2: Install Dependencies

Run the following command in a Google Colab notebook cell:

```python
%pip install -U langchain langchain-community
%pip install langchain-text-splitters
%pip install langchain-huggingface
%pip install langchain-google-genai
%pip install chromadb
%pip install sentence-transformers
%pip install protobuf
```

If you encounter dependency conflicts, restart the Colab runtime and rerun the notebook cells.

### Step 3: Configure the Google API Key

Obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/).

For a quick local test, configure the key as follows:

```python
import os
from getpass import getpass

GOOGLE_API_KEY = getpass("Enter your Google API key: ")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
```

Do not commit your API key to GitHub. For a more secure setup, use Google Colab Secrets or environment variables.

### Step 4: Upload the JSON Dataset

Upload `menu_incoming_json_log.json` to Google Colab using the Files panel, or mount Google Drive if the file is stored there.

The expected path in the notebook is:

```python
file_path = "/content/menu_incoming_json_log.json"
```

Update this path if your file is stored elsewhere.

### Step 5: Run the Notebook

Execute the notebook cells in order to:

1. Initialize the Gemini model.
2. Load and split the JSON menu data.
3. Create Hugging Face embeddings.
4. Build the ChromaDB retriever.
5. Initialize the LangChain RetrievalQA chain.
6. Submit a question and display the response.

## 💡 Example Usage

Example query:

```python
question = "Give me a variety of Jain thali food"

result = qa_chain.invoke({"query": question})

print(result["result"])
```

The system retrieves relevant menu information and generates an answer using the available context.

**Note:** The actual response depends on the contents of the JSON dataset. The application should not be expected to recommend menu items that are absent from the retrieved information.

## 🔍 Key Features

- **Natural Language Queries:** Ask food-related questions in everyday language.
- **Semantic Search:** Retrieve relevant menu information based on meaning rather than exact keyword matches.
- **Context-Aware Responses:** Generate answers using retrieved menu information.
- **JSON Data Support:** Process structured food menu data.
- **Customizable Retrieval:** Configure the number of retrieved chunks using the `k` parameter.
- **Source Document Retrieval:** Return source documents alongside the generated answer for further inspection.
- **Modular Architecture:** Extend the application to support additional menus and food-related use cases.

## 🔐 Security Considerations

- Keep Google Gemini API keys private.
- Never upload API keys or other secrets to a public repository.
- Use environment variables or Colab Secrets to manage credentials.
- Check API usage limits and billing requirements before deploying the application.

## 🚀 Future Enhancements

- Build an interactive web interface using Streamlit.
- Add filters for Jain, vegetarian, vegan, and other dietary preferences.
- Include food prices, ingredients, allergens, and nutritional information where available.
- Display source menu entries for transparency.
- Support PDF and multiple JSON menu files.
- Add persistent ChromaDB storage to avoid rebuilding the index on every run.
- Implement chat history for multi-turn conversations.
- Add automated tests for retrieval quality and answer accuracy.

## 🎓 Learning Outcomes

This project demonstrates practical implementation of:

- Retrieval-Augmented Generation (RAG).
- Large Language Model (LLM) integration.
- Semantic search and vector embeddings.
- Vector databases and similarity retrieval.
- Structured JSON data processing.
- Prompt engineering and context-grounded question answering.
- LangChain-based AI application development.
This project can be distributed under the MIT License. If you choose this license, add a `LICENSE` file to the repository and ensure that you have the rights to distribute the dataset and other included resources.
