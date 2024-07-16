import streamlit as st
from model_loader import get_response

# Streamlit App
def main():
    st.title('Website Chatbot')

    user_input = st.text_input('You:')
    if user_input:
        # Assume `content` is pre-scraped and processed
        context = ' '.join(content)
        
        response = get_response(user_input, context)
        st.text_area('Bot:', value=response, height=200)

if __name__ == "__main__":
    main()
