import os
import openai

openai.api_key = "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" 
# os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="hello\n",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].text)