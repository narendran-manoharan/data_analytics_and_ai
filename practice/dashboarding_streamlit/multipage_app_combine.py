import streamlit as st
from multipage_app import Multipage

from multipage_app_page1 import page1_body

from multipage_app_page2 import page2_body

app = Multipage(app_name="This is my first app in Streamlit!")

app.add_page("page 1", page1_body)
app.add_page("page 2", page2_body)

app.run()