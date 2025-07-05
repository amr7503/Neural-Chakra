import streamlit as st
import requests
from hydra import initialize, compose
from hydra.core.global_hydra import GlobalHydra

# Clear Hydra state and initialize
GlobalHydra.instance().clear()
initialize(config_path="conf")
cfg = compose(config_name="config")

# Page config
st.set_page_config(
    page_title="Odia Legal Assistant",
    page_icon="⚖️",
    layout="centered"
)

# Custom CSS fixes
st.markdown("""
<style>
    /* Fix typing visibility */
    .stTextInput input, .stTextArea textarea {
        color: black !important;
        font-size: 1rem !important;
    }
    
    /* Odia font support */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Odia&display=swap');
    .odia {
        font-family: 'Noto Sans Odia' !important;
    }
</style>
""", unsafe_allow_html=True)

# Session state setup
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.language = "Odia"
    st.session_state.model = "anthropic/claude-3-sonnet"

# Sidebar controls
with st.sidebar:
    st.session_state.language = st.radio(
        "Language",
        ["Odia", "English"],
        index=0 if st.session_state.language == "Odia" else 1
    )
    
    st.session_state.model = st.selectbox(
        "AI Model",
        ["anthropic/claude-3-sonnet", "google/gemini-2.5-pro", "openai/gpt-4"],
        index=["anthropic/claude-3-sonnet", "google/gemini-2.5-pro", "openai/gpt-4"].index(st.session_state.model)
    )

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if st.session_state.language == "Odia":
            st.markdown(f'<div class="odia">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(msg["content"])

# Chat input with immediate echo
if prompt := st.chat_input("ଆପଣଙ୍କର ପ୍ରଶ୍ନ ଲେଖନ୍ତୁ..." if st.session_state.language == "Odia" else "Type your question..."):
    # Immediately show user input
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get AI response
    with st.chat_message("assistant"):
        try:
            with st.spinner("ଚିନ୍ତା କରୁଛି..." if st.session_state.language == "Odia" else "Thinking..."):
                response = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {cfg.api.openrouter_key}",
                        "HTTP-Referer": st.query_params.get("url", "https://legal-ai.streamlit.app"),
                        "X-Title": "Odia Legal Assistant"
                    },
                    json={
                        "model": st.session_state.model,
                        "messages": [
                            {
                                "role": "system",
                                "content": "You are a legal assistant for Indian law. Respond in Odia if asked in Odia, otherwise English."
                            },
                            *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                        ],
                        "temperature": 0.3
                    },
                    timeout=30
                )
                response.raise_for_status()
                reply = response.json()["choices"][0]["message"]["content"]
                
                if st.session_state.language == "Odia":
                    st.markdown(f'<div class="odia">{reply}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(reply)
                
                st.session_state.messages.append({"role": "assistant", "content": reply})
                
        except Exception as e:
            error_msg = "କ୍ଷମା କରିବେ, ସେଭର୍ ତ୍ରୁଟି ଘଟିଛି" if st.session_state.language == "Odia" else "Server error occurred"
            st.error(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})