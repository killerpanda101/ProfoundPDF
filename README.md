# ChatPDF 📄✨

Welcome to ChatPDF - your interactive PDF assistant powered by OpenAI's cutting-edge language model! ChatPDF enables you to interact with your PDFs in a whole new way, extracting information, summarizing content, and much more.

## Getting Started 🚀

### Step 1: Obtain Your API Key 🔑

To interact with the OpenAI model, you will need an API key. Follow these steps to obtain one:

1. Visit the [OpenAI website](https://openai.com).
2. Sign up for an account if you don't already have one.
3. Navigate to the API section and follow the instructions to generate your API key.

### Step 2: Set Your API Key 🛠️

Once you have your API key, you'll need to configure the application to use it. In the `app.py` file, find the line that looks like this:

```python
os.environ["OPENAI_API_KEY"] = "sk-r7QTNcbEeRBAub8quuJAT3BlbkFJQNnPTgSaUVvGhxxxx"
```

Replace the placeholder key with your actual API key.

### Step 3: Install Dependencies 📦

ChatPDF requires several dependencies to run. Install them using the provided `requirements.txt` file with the following command:

```bash
pip install -r requirements.txt
```

### Step 4: Launch the Application 🌟

With your API key set & dependencies installed, you're ready to start the application. Navigate to the root folder of the directory and run:

```bash
streamlit run app.py
```

The application should now be up and running on your local server. Open your web browser and go to the address indicated by Streamlit (usually `http://localhost:8501`) to start using ChatPDF.

## Features 🌈

ChatPDF comes with a plethora of features designed to make your interaction with PDF documents as smooth as possible:

- **Information Extraction**: Pull out key details or data from your PDF files.
- **Content Summarization**: Get concise summaries of lengthy documents.
- **Q&A with your PDF**: Ask questions and get answers based on the content of your PDFs.
