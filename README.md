
**DailyAgent-AIAgent** is an AI-powered assistant designed to answer questions based on your daily journal entries. It uses Retrieval-Augmented Generation (RAG) to understand and respond to queries using the contents of `DailyLogs.txt`.

## How It Works

- `DailyLogs.txt` is your daily journal file.
- Add one or two lines each day describing your work or thoughts.
- The agent uses this file to answer your questions about past entries.

## Getting Started

1. Make sure `DailyLogs.txt` is in the same folder as `main.py`.
2. Add HuggingFace token value in .env
3. Run the script:

   ```bash
   python main.py

# Examples

> Ask something about your logs (or type 'exit'): When is my PTO?
Answer: 
Your PTO is scheduled from July 1st to July 5th.

> Ask something about your logs (or type 'exit'): When is the next follow-up with the GCP team?
Answer:
The next follow-up with the GCP team was scheduled for 4 days after the meeting on 6/15. So, the next follow-up would be on 6/19.


