import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

# GPT-3 completion function
def ask_gpt3(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        stop=None,
    )
    return response.choices[0].text.strip()

# Streamlit app
def main():
    st.title("Music Chat with ChatGPT")

    st.write("Welcome! Ask me anything about music.")

    user_input = st.text_input("You:", "")

    if st.button("Ask"):
        if user_input:
            with st.spinner("Thinking..."):
                response = ask_gpt3(user_input)
            st.write("ChatGPT:", response)
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()