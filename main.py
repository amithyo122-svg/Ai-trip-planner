from dotenv import load_dotenv
from crew import travel_crew

load_dotenv()


def run():
    print("🌍 AI Travel Planner")
    print("Type 'exit' to quit.\n")

    conversation = []

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        conversation.append(f"User: {user_input}")

        result = travel_crew.kickoff(
            inputs={
                "conversation": "\n".join(conversation)
            }
        )

        print(f"\nAI: {result}\n")

        conversation.append(f"AI: {result}")


if __name__ == "__main__":
    run()
