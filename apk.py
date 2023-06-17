import openai

openai.api_key = 'YOUR_API_KEY'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

print("ChatGPT: Hello! How can I assist you today?")

while True:
    user_input = input("User: ")
    if user_input.lower() == "bye":
        break
    response = chat_with_gpt("User: " + user_input + "\nChatGPT:")
    print("ChatGPT:", response)
