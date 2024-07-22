import openai

# Set up your API key
openai.api_key = 'you own api here'

# Define a function to get a response from the model
def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Updated model name
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

# Main loop to interact with the user
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    response = get_response(user_input)
    print("ChatGPT:", response)


#hell

