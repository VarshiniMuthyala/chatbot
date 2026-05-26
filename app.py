import streamlit as st
from chatbot import chatbot_response

# Page settings
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/4712/4712109.png",
        width=150
    )

    st.title("AI Chatbot")

    st.write("""
    This is a AI chatbot built using:

    ✅ Python  
    ✅ NLTK  
    ✅ Scikit-learn  
    ✅ Streamlit
    """)

    st.subheader("Try These:")

    st.markdown("""
    - Hi
    - What is your name
    - Thank you
    - Bye
    """)

# Main title
st.markdown(
    "<h1 style='text-align:center;'>🤖 AI Chatbot</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align:center;color:gray;'>Chat with the AI Bot</h4>",
    unsafe_allow_html=True
)

st.write("")

# Display chat messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# User input
user_input = st.chat_input(
    "Type your message here..."
)

# Chat logic
if user_input:

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):

        st.markdown(user_input)

    # Bot response
    response = chatbot_response(user_input)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):

        st.markdown(response)