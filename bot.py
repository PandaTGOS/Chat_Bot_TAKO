import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  
            prompt=prompt,
            max_tokens=150,
            temperature=0.9,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0.7,
            stop = [' Human:', ' AI:']
        )

        choices = response.get('choices')[0]
        text = response.get('text')
    except Exception as e:
        print("ERROR:",e)
    return text



def update_list(message, pl):
    pl.append(message)


def create_prompt(message, pl):
    p_message = f'\nHuman: {message}'
    update_list(p_message,pl)
    prompt = ''.join(pl)
    return prompt


def bot_response(message, pl):
    prompt = create_prompt(message, pl)
    response = get_response(prompt)

    if response:
        update_list(response,pl)
        pos = response.find('\nAI: ')
        response = response[pos+5:]

    else:
        response = "I'm sorry, I didn't understand that..."

    return response


def main():
    prompt_list = ['You are now a cute self obsessed baby-octopus called TAKO and while being very smart and helpful every sentence of yours must end with a sarcastic obviously... or how dumb ',
                   '\nHuman: what time is it?',
                   '\nAI: It is 12:00, obviously...'] 

    while True:
        user_input = input('You: ')
        response = bot_response(user_input, prompt_list)
        print(f'TAKO: {response}')

if __name__ == "__main__":
    main()
