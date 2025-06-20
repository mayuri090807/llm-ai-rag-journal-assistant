from dotenv import load_dotenv
from rag import build_vectorstore, ask_question

if __name__ == "__main__":
    file_path = r"C:\Git\rag-journal-assistant\DailyLogs.txt"  # Your daily log file path
    vectorstore = build_vectorstore(file_path)

    while True:
        question = input("\nAsk something about your logs (or type 'exit'): ")
        if question.lower() == "exit":
            break

        answer, sources = ask_question(vectorstore, question)
        print("\nAnswer:\n", answer)
        print("\nSources:")
        for doc in sources:
            print("-", doc.page_content[:100].replace("\n", " "), "...")
