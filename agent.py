from langchain_ollama import ChatOllama

model = ChatOllama(
    model="llama3.2",
    temperature=0
)

print("=" * 60)
print("           SIMPLE LANGCHAIN AI ASSISTANT")
print("=" * 60)
print("Ask me anything.")
print("Type 'exit' to stop.")
print()

while True:
    question = input("You: ").strip()

    if question.lower() in ["exit", "quit"]:
        print("\nGoodbye!")
        break

    if not question:
        continue

    try:
        response = model.invoke(
            [
                (
                    "system",
                    "You are a helpful AI assistant. "
                    "Answer the user's questions clearly and accurately."
                ),
                ("human", question)
            ]
        )

        print("\nAgent:")
        print(response.content)
        print()

    except Exception as e:
        print("\nERROR:")
        print(type(e).__name__)
        print(str(e))
        print()