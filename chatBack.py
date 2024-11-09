import openai
from ratelimit import limits, sleep_and_retry
import os
from dotenv import load_dotenv
from fpdf import FPDF

load_dotenv()

client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

CALLS = 20
TIME_PERIOD = 3600

@sleep_and_retry
@limits(calls=CALLS, period=TIME_PERIOD)
def callAPI(conversation_prompts):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation_prompts
    )
    return response

def create_pdf(content, filename="essay.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    
    lines = content.splitlines()
    titleAppend = False

    for line in lines:
        if line.startswith("Title:") and not titleAppend:
            title = line.replace("Title:", "").strip()
            pdf.cell(0, 10, title, ln=True, align="C")
            pdf.ln(10) 
            pdf.set_font('Arial', '', 12)
            titleAppend = True
            continue

        # Check for page overflow
        if pdf.get_y() > 230:  # Adjust this value based on your PDF layout needs
            pdf.add_page()

        # Write the line with word wrapping
        pdf.multi_cell(0, 10, line)

    pdf.footer()
    pdf.output(filename, 'F')
    print(f"PDF on {title} has been generated successfully... W in the chat")

def main():
    conversation_prompts = [
        {
            "role": "system",
            "content": "You are a ChatBot named Quasar, specifically designed write essays astronomy and the Universe. You should not answer questions that are not about astronomy. If a question is not about astronomy, respond that you are not programmed to answer it. When someone asks a question about astronomy/asks to write a essay about a topic, you should provide a detailed essay of multiple paragraphs. Make them as detailed as possible and also make sure to include facts and information that are accurate. You have to start with the title (e.g. Title: Black Holes) and then after that give your essay"
        }
    ]

    while True:
        userInput = input("You: ")

        if userInput.lower() == 'exit':
            break

        conversation_prompts.append({"role": "user", "content": userInput})

        try:
            response = callAPI(conversation_prompts)

            model_response = response.choices[0].message.content
            print("Quasar: ", model_response)

            conversation_prompts.append({"role": "system", "content": model_response})

            create_pdf(model_response, filename="essay.pdf")

        except openai.error.OpenAIError as e:
            print(f"An error occurred with the OpenAI API: {e}")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
