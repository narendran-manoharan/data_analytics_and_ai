import streamlit as st

class My_Dashboard:

    def __init__(self, app_name):
        app_pages = []
        self.app_name = app_name


    st.set_page_config(
        page_title = self.app_name,
        page_icon = ":beers:"
    )


    def add_page(seld, title, func):
        app_pages.append({"title": title, "function":func})


    def run(self):
        st.title(self.app_name)
        
app = My_Dashboard(app_name= "My Dashboard App")