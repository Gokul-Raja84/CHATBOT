# Import the required libraries
import openai
import gradio

# Set your OpenAI API key
openai.api_key = "OPENAI API key"

# Define the initial system message
messages = [{"role": "system", "content": "A  Helpful AI Assistant"}]


# Define the chatbot function
def CustomChatGPT(user_input):
    # Append the user's input to the messages list
    messages.append({"role": "user", "content": user_input})

    # Use the OpenAI API to get the chatbot's response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Extract the chatbot's reply from the API response
    ChatGPT_reply = response["choices"][0]["message"]["content"]

    # Append the chatbot's reply to the messages list
    messages.append({"role": "assistant", "content": ChatGPT_reply})

    # Return the chatbot's response
    return ChatGPT_reply


# Create the Gradio interface
demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="CHATBOT by GOKUL RAJA")

# Launch the Gradio interface
demo.launch(share=True)