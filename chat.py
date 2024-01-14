# import openai;

# openai.api_key = "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"
# question=input("WHat you wanna Ask")
# response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt=question,
#     temperature=0.7,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
# )
# print(response)



# user_input = "How does photosynthesis work?"

# response = openai.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": user_input}
#     ],
#     temperature=1,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
# )

# # Extract and print the model's reply
# reply = response['choices'][0]['message']['content']
# print(reply)


import openai

# Set your OpenAI API key
openai.api_key = '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'


# # Define the function to call the OpenAI API
# def call_openai_api(prompt):
#     response = openai.Completion.create(
#         engine='gpt-3.5-turbo-1106',
#         prompt=prompt,
#         max_tokens=100
#     )
#     return response.choices[0].text.strip()

# # Example usage

# # Example usage
# prompt = 'what is photo synthesys'
# response = call_openai_api(prompt)
# print(response)

import openai
openai.api_key = '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'
MODEL= "gpt-3.5-turbo"
# example with a system message
response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "who is donald trump"},
    ],
    temperature=0,
)

print(response['choices'][0]['message']['content'])

