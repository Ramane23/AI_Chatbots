"""
This module defines the LoadStreamlitUI class that initializes configuration,
renders a Streamlit user interface, and collects user inputs such as LLM selection,
model selection, API keys, and use cases.
"""

import streamlit as st  # Streamlit library for building interactive web apps
import os  # OS module for interacting with the operating system (not used here but imported)

from src.frontend.uiconfigfile import Config  # Import the Config class for app configurations

class LoadStreamlitUI:
    """
    Class to load and manage the Streamlit UI for the application.
    It handles configuration loading and user input collection.
    """

    def __init__(self):
        """
        Initializes the LoadStreamlitUI instance:
        - Creates a Config object for app settings.
        - Initializes an empty dictionary to store user selections.
        """
        self.config = Config()  # Instantiate Config object to access settings and options
        self.user_controls = {}  # Dictionary to store user input selections

    def load_streamlit_ui(self):
        """
        Renders the Streamlit UI components:
        - Sets the page title and layout.
        - Displays a header.
        - Shows a sidebar with dropdowns for LLM selection, model selection (if Groq),
          API key input, and use case selection.
        - Validates the API key input for Groq LLM.
        
        Returns:
            dict: A dictionary containing the user selections.
        """
        # Configure the Streamlit page title and layout to wide format
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout="wide")

        # Display the main header with a robot emoji and page title
        st.header("🤖 " + self.config.get_page_title())

        # Sidebar block for user input controls
        with st.sidebar:
            # Retrieve the available LLM options from configuration
            llm_options = self.config.get_llm_options()
            # Retrieve the available use case options from configuration
            usecase_options = self.config.get_usecase_options()

            # Dropdown menu for selecting the LLM (Language Model)
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            # If the selected LLM is 'Groq', show additional options
            if self.user_controls["selected_llm"] == 'Groq':
                # Retrieve Groq-specific model options
                model_options = self.config.get_groq_model_options()
                # Dropdown menu for selecting the Groq model
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                # Password input field for the GROQ API key; also saved to session state
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")
                # If API key is missing, display a warning message with a reference link
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")

            # Dropdown menu for selecting use cases
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)
            
            if self.user_controls["selected_usecase"] =="Chatbot With Web":
                os.environ["TAVILY_API_KEY"]=self.user_controls["TAVILY_API_KEY"]=st.session_state["TAVILY_API_KEY"]=st.text_input("TAVILY API KEY",type="password")

                # Validate API key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please enter your TAVILY_API_KEY key to proceed. Don't have? refer : https://app.tavily.com/home")

            if self.user_controls['selected_usecase']=="AI News":
                st.subheader("📰 AI News Explorer ")
                
                with st.sidebar:
                    time_frame = st.selectbox(
                        "📅 Select Time Frame",
                        ["Daily", "Weekly", "Monthly"],
                        index=0
                    )
                if st.button("🔍 Fetch Latest AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame
                    
        # Return the dictionary of all user-selected controls
        return self.user_controls
