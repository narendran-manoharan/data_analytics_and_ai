import streamlit as st  # Import Streamlit for building interactive web apps

class Multipage:
    def __init__(self, app_name) -> None:
        # Initialize the Multipage app with a given name.
        # This constructor sets up the app's configuration and prepares a container for pages.
        self.pages = []  # List to hold all registered pages (each as a dict)
        self.app_name = app_name  # Store the app's display name

        # Configure the Streamlit app's browser tab with a title and icon.
        # This improves user experience and branding.
        st.set_page_config(
            page_title=self.app_name,   # Sets the browser tab's title
            page_icon=":computer:"      # Sets the browser tab's icon (emoji for visual appeal)
        )

    def add_page(self, title, func) -> None:
        # Register a new page to the multipage app.
        # Each page is represented as a dictionary with a title and a function to render its content.
        # This design allows for flexible addition of any callable as a page.
        self.pages.append({"title": title, "function": func})

    def run(self):
        # Main entry point to render the app.
        # Displays the app's title and provides a sidebar for navigation between pages.

        st.title(self.app_name)  # Show the app's name at the top for context

        # Sidebar navigation: users select which page to view using radio buttons.
        # The radio displays only the page titles for clarity.
        page = st.sidebar.radio(
            "Menu", 
            self.pages, 
            format_func=lambda page: page["title"]  # Only show the title in the sidebar
        )

        # Render the selected page by calling its associated function.
        # This allows each page to have its own layout and logic.
        page["function"]()