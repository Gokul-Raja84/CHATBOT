import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Initialize an empty list to store chat messages
messages = []

# Prompt the user to specify the type of chatbot they want to create
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

# Inform the user that the chatbot is ready
print("Your new assistant is ready!")

# Start a loop to keep the conversation going until the user types "quit()"
while True:
    message = input()  # Take input from the user
    messages.append({"role": "user", "content": message})  # Add user message to the list of messages
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the GPT-3.5-turbo model for chat completion
        messages=messages)  # Send the list of messages to OpenAI API
    reply = response["choices"][0]["message"]["content"]  # Get the assistant's reply from the API response
    messages.append({"role": "assistant", "content": reply})  # Add assistant's reply to the list of messages
    print("\n" + reply + "\n")