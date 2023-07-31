import openai

openai.api_key = "(OPENAI API KEY)"  # Insert your own openai API secret key

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me ideas for apps and services I could build with openai apis"}])
print(completion.choices[0].message.content)

# Change the content prompt as per your way