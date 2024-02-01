from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def main():
    prompt = "Hello, what is your name, and what is your function ?"
    response = client.chat.completions.create(model="gpt-3.5-turbo-1106",
    messages=[
        {"role": "system", "content": "You are a ChatBot named Quasar, meant to give the user information about astronomy and our Universe."},
        {"role": "user", "content": prompt}
    ])

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
