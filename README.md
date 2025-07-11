
This is an AI-powered assistant designed to answer questions based on the daily journal entries. It uses Retrieval-Augmented Generation (RAG) to understand and respond to queries using the contents of `DailyLogs.txt`.

## How It Works
Here's is the simplied breakdown of the workflow -
- Load: loads the content from `DailyLogs.txt` file.
- Split: The text is broken down into smaller, manageable chunks.
- Embed & Store: These chunks are converted into embeddings and stored in an in-memory FAISS vector database.
- Retrieve: Query is also converted into an embedding. The system then searches the vector database to find the text chunks from the journal that are most semantically similar to the question.
- Generate: The original question and the retrieved text chunks are combined into a single prompt. This combined prompt is then sent to the LLM model (microsoft/Phi-3-mini-4k-instruct in this case). The LLM uses the provided context from journal to generate a relevant and accurate answer.

## Requirements
- Python 3.8+
- A .env file with your Hugging Face token

## Getting Started

1. Add one or two lines each day describing your work or thoughts in `DailyLogs.txt`. Keep this file in the same folder as `main.py`
2. Add HuggingFace token value in .env
3. Run the script:

   ```bash
   python main.py

# Examples

Example 1:
> Ask something about your logs (or type 'exit'): When is my PTO?

> Answer: 

> Your PTO is scheduled from July 1st to July 5th.

Example 2:

> Ask something about your logs (or type 'exit'): When is the next follow-up with the GCP team?

> Answer:

> The next follow-up with the GCP team was scheduled for 4 days after the meeting on 6/15. So, the next follow-up would be on 6/19.

# Next steps
- Use enternal database to store embeddings
- Import data from multiple files
- Scaling

