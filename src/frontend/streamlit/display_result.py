"""
This module defines the DisplayResultStreamlit class, which handles
the display of chatbot interactions using Streamlit for the given use case.
"""

import streamlit as st  # Streamlit for interactive web UI
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage  # Message types from LangChain
import json  # Standard library for working with JSON data (not used here yet, but can help with serialization)


class DisplayResultStreamlit:
    """
    Class responsible for displaying chatbot results in Streamlit based on the selected use case.
    """

    def __init__(self, usecase, graph, user_message):
        """
        Initializes the DisplayResultStreamlit object with user-specified parameters.

        Args:
            usecase (str): The selected use case (e.g., "Basic Chatbot").
            graph (object): The LangChain graph or flow object responsible for processing the messages.
            user_message (str): The input message from the user.
        """
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        """
        Displays the chatbot interaction on the Streamlit UI.

        If the use case is "Basic Chatbot", it streams the response from the graph
        and renders both user and assistant messages in a conversational layout.
        """
        # Assign instance variables to local variables for readability
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        # Log the incoming user message to the console for debugging
        print(user_message)

        # Check if the selected use case is "Basic Chatbot"
        if usecase == "Basic Chatbot":
            # Send the user message to the graph and stream responses
            for event in graph.stream({'messages': ("user", user_message)}):
                print(event.values())  # Debug print of streamed events

                # Iterate over all values in the event stream
                for value in event.values():
                    print(value['messages'])  # Debug print of the assistant message

                    # Display user's message in the UI as a chat bubble
                    with st.chat_message("user"):
                        st.write(user_message)

                    # Display assistant's response in the UI
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)
