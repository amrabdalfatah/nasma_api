# import openai
# from django.conf import settings

# openai.api_key = settings.APIKEY
from openai import OpenAI

client = OpenAI(
  api_key=""
)

def send_message_to_api(message):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    store=True,
    messages=[
      {"role": "user", "content": "write a haiku about ai"}
    ]
  )

  return completion.choices[0].message.content
  # res = openai.chat.completions.create(
  #   model="gpt-4o-mini",
  #   store=True,
  #   messages=[
  #     {"role": "system", "content": "meditation and yoga"},
  #     {"role": "user", "content": "{message}"}
  #   ],
  # )
  # return res.choices[0].message.content