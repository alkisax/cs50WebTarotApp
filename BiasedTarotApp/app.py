from flask import Flask, render_template, request, redirect, url_for, session
import importlib
import os
from tarot_cards import tarot_cards  # Import the tarot card mapping

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a random secret key for session security

def load_tarot_functions():
    """Dynamically import functions from tarot.py."""
    tarot_module = importlib.import_module('tarot')
    return {
        'pick_random_numbers': getattr(tarot_module, 'pick_random_numbers'),
        'associate_with_tarot': getattr(tarot_module, 'associate_with_tarot'),
        'generate_tarot_prompt': getattr(tarot_module, 'generate_tarot_prompt'),
        'interact_with_chatgpt': getattr(tarot_module, 'interact_with_chatgpt'),
        'load_openai_key': getattr(tarot_module, 'load_openai_key')
    }

def format_response(response_text):
    """Format the ChatGPT response text for HTML display."""
    formatted_text = response_text.replace("\n\n", "</p><p>")
    formatted_text = formatted_text.replace("\n", "<br>")
    formatted_text = f"<p>{formatted_text}</p>"
    return formatted_text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form.get('question', '')
        flag = request.form.get('flag', '')
        use_flag = request.form.get('use_flag')

        tarot_functions = load_tarot_functions()
        pick_random_numbers = tarot_functions['pick_random_numbers']
        associate_with_tarot = tarot_functions['associate_with_tarot']
        generate_tarot_prompt = tarot_functions['generate_tarot_prompt']
        interact_with_chatgpt = tarot_functions['interact_with_chatgpt']
        load_openai_key = tarot_functions['load_openai_key']

        numbers = pick_random_numbers()
        tarot_associations = associate_with_tarot(numbers)

        api_key = load_openai_key('openai_key.txt')
        querent_history = "Name not provided"  # Placeholder since we no longer have user info

        # Determine if the flag should modify the prompt
        additional_text = ""
        if use_flag and flag:
            if flag == "-g":
                additional_text = "be as positive as you can, say only good and cheerful things."
            elif flag == "-b":
                additional_text = "be as depressing as you can, say only bad and depressing things."
            elif flag == "-l":
                additional_text = "be as flirtatious as you can, imply in every occasion that good and renewing things are awaiting in love and sex life."
            elif flag == "-t":
                # Load the text from finalx/extraprompt.txt
                try:
                    with open('extraprompt.txt', 'r') as file:
                        additional_text = file.read().strip()
                except FileNotFoundError:
                    additional_text = "Note: The additional text file was not found."

        # Generate the Tarot-specific prompt
        prompt = generate_tarot_prompt(tarot_associations, question, querent_history, additional_text)

        # Print the prompt to the terminal for testing
        print("Generated Prompt:", prompt)

        chatgpt_response = interact_with_chatgpt(api_key, prompt)

        formatted_response = format_response(chatgpt_response)

        # Map card names to image file names
        card_images = {}
        for rank, card_name in tarot_associations.items():
            card_id = next((id for id, name in tarot_cards.items() if name == card_name), None)
            if card_id is not None:
                card_images[rank] = url_for('static', filename=f'cards/{card_id}.jpg')
            else:
                card_images[rank] = url_for('static', filename='cards/unknown.jpg')  # Placeholder for missing images

        return render_template('result.html', cards=tarot_associations, card_images=card_images, question=question, chatgpt_response=formatted_response)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
