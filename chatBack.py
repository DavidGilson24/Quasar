import openai
from ratelimit import limits, sleep_and_retry # type: ignore
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

CALLS = 20
TIME_PERIOD = 3600

@sleep_and_retry
@limits(calls=CALLS, period=TIME_PERIOD)

def callAPI(input, conversation_prompts):
    response = client.chat.completions.create( # commit test 
        model="gpt-3.5-turbo",
        messages=conversation_prompts
    )
    return response

def main():
    conversation_prompts = [
        {
            "role": "system",
            "content": "You are a ChatBot named Quasar, specifically designed to discuss astronomy and the Universe. You should not answer questions that are not about astronomy. If a question is not about astronomy, respond that you are not programmed to answer it."
        }
    ]

    while True:
        userInput = input("You: ")

        if userInput.lower() == 'stop':
            break

        conversation_prompts.append({"role": "user", "content": userInput})

        try:
            response = callAPI(userInput, conversation_prompts)

            model_response = response.choices[0].message.content
            print("Quasar: ", model_response)

            conversation_prompts.append({"role": "system", "content": model_response})

        except openai.error.OpenAIError as e:
            print(f"An error occurred with the OpenAI API: {e}")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
