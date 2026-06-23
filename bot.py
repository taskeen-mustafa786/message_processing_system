import streamlit as st
from groq import Groq
import json

client = Groq(api_key="API_KEY")

def analyze_message(message):

    prompt = f"""
Return JSON only:
{{
  "intent": "complaint | refund/return | sales inquiry | delivery question | account/technical issue | general query | spam",
  "sentiment": "positive | negative | neutral",
  "auto_reply": "short professional reply"
}}

Message:
\"\"\"{message}\"\"\"
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Return only JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return json.loads(response.choices[0].message.content)


st.title("AI Message Classifier")

msg = st.text_area("Enter message")

if st.button("Analyze"):
    result = analyze_message(msg)
    st.json(result)