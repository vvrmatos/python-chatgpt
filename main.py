import openai

# add/create your api key: https://platform.openai.com/account/api-keys
client = openai.OpenAI(api_key='')

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": "Give me some Hello World C code"}
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)
