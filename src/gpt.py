from openai import OpenAI

import sys
import os

def gpt_proompt(system_proompt, proompt):
    key = os.getenv("OPENAI_API_KEY")
    if key is None:
        print("Error: Variable OPENAI_API_KEY is not set.\n Use export OPENAI_API_KEY=<your key>")
        sys.exit(1)
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    r = client.chat.completions.create(model="gpt-3.5-turbo-1106",
    #model="gpt-4",
    messages=[
        {"role": "system", "content": system_proompt},
        {"role": "user", "content": proompt}
    ])

    text = r.choices[0].message.content

    return text