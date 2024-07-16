import streamlit as st
from model_loader import get_response, scrape_website

# Example usage to scrape website and get content
base_url = 'http://www.trimble.com'
content = scrape_website(base_url)

# Streamlit App
def main():
    st.title('Website Chatbot')

    user_input = st.text_input('You:')
    if user_input:
        # Join content only when user input is provided
        context = ' '.join(content)
        
        response = get_response(user_input, context)
        st.text_area('Bot:', value=response, height=200)

if __name__ == "__main__":
    main()
