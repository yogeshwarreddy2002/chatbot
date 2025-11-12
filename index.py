from google import genai
import streamlit as st
st.title("🤖Smart Chat Bot")
st.header("AI Chat Assistant")
with st.sidebar:
    st.title("⚙️ Settings")
    st.write("This is your AI Chat Assistant.")
    st.write("You can ask general knowledge, coding, help, ideas, etc.")
    st.write("---")
user_prompt=st.text_input("Enter your prompt: ")
send_button=st.button("send")
if user_prompt and send_button:
 client = genai.Client(api_key="AIzaSyBdlcmcff1X7CUMgzar8P7rvV0XHQGf2YI")
 response = client.models.generate_content(
 model="gemini-2.5-flash", contents=user_prompt
  )
 st.title("AI Response:")
 st.write(response.text)







