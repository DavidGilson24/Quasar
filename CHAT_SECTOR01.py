from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def main():
    conversationPrompts = [
        {"role": "system", "content": "You are a ChatBot named Quasar, specifically designed to discuss astronomy and the Universe. You should not answer questions that are not about astronomy. If a question is not about astronomy, respond that you are not programmed to answer it. If someone asks who programmed or built you, you say 'David Gilson'"}
    ]

    while True:
        try:
            userInput = input("You: ")

            if userInput.lower() == 'stop':
                break

            conversationPrompts.append({"role": "user", "content": userInput})

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=conversationPrompts
            )

            modelResponse = response.choices[0].message.content
            print("Quasar: ", modelResponse)
            
            conversationPrompts.append({"role": "system", "content": modelResponse})

        except OpenAI.error.OpenAIError as e:
            print(f"An error occurred: {e}")
            

if __name__ == "__main__":
    main()
