import streamlit as st
from openai import OpenAI

client = OpenAI()

#  GPT-3 completion function
def ask_gpt(user_input):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a music expert giving in-depth explanations."},
        {"role": "user", "content": user_input}
    ]
    )
    return completion.choices[0].message.content


# Streamlit app
def main():

    st.title("Music Chat with ChatGPT")

    st.write("Welcome! Ask me anything about music.")

    user_input = st.text_input("You:", "")

    if st.button("Ask"):
        if user_input:
            with st.spinner("Thinking..."):
                response = ask_gpt(user_input)
            st.write("ChatGPT:", response)
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()