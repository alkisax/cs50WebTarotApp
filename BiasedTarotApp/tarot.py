import random
import openai
import logging
from tarot_cards import tarot_cards

# Configure logging to suppress debug messages from OpenAI API
logging.basicConfig(level=logging.WARNING)  # Set the default logging level to WARNING

def pick_random_numbers():
    """Generate three random numbers between 1 and 78 and rank them as 1st, 2nd, and 3rd."""
    numbers = random.sample(range(1, 79), 3)
    numbers.sort()
    return numbers

def associate_with_tarot(numbers):
    """Associate the given numbers with their corresponding Tarot cards."""
    tarot_associations = {f"{i+1}st": tarot_cards[num] for i, num in enumerate(numbers)}
    return tarot_associations

def load_openai_key(file_path):
    """Load the OpenAI API key from a text file."""
    with open(file_path, 'r') as file:
        api_key = file.read().strip()
    return api_key

def generate_tarot_prompt(tarot_associations, question, querent_history=None, additional_text=None):
    """
    Generate the prompt for Tarot card reading.

    :param tarot_associations: A dictionary of ranked Tarot cards.
    :param question: The question for the Tarot reading.
    :param querent_history: Optional background information about the querent.
    :param additional_text: Optional additional instructions or context to include in the prompt.
    :return: A formatted prompt string for ChatGPT.
    """
    # Prepare the Tarot card details
    tarot_cards_input = "\n".join([f"{rank}: {card}" for rank, card in tarot_associations.items()])

    # Create the specialized Tarot reading prompt
    tarot_prompt = (
        "You are a Tarot interpreter. Provide a detailed interpretation of the following Tarot cards in direct response to the "
        "question asked. For each card, describe its meaning thoroughly and explain its relevance to the question. After "
        "interpreting each card individually, provide a combined interpretation that synthesizes the meanings of all the cards in "
        "relation to the question asked. "
        "Avoid any introductory or contextual information, and focus solely on delivering a profound and insightful analysis of the "
        "individual cards and their combined significance. Do not refer to yourself or anything outside of the Tarot cards and their meanings."
    )

    # Add querent history if provided
    if querent_history:
        tarot_prompt += f" Consider the following background information: {querent_history}. "

    # Add additional text if provided
    if additional_text:
        tarot_prompt += f" {additional_text}"

    # Finalize the Tarot prompt
    tarot_prompt += (
        f"\n\nTarot Cards:\n{tarot_cards_input}\n\nQuestion: {question}"
    )

    return tarot_prompt

def interact_with_chatgpt(api_key, combined_prompt):
    """Connect to OpenAI's ChatGPT and send the prompt."""
    openai.api_key = api_key

    # Send the combined prompt to ChatGPT using the gpt-3.5-turbo model
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": combined_prompt}
        ],
        max_tokens=500,  # Increased token limit for more detailed responses
        temperature=0.7
    )

    # Get the response from ChatGPT
    answer = response.choices[0].message['content'].strip()
    return answer
