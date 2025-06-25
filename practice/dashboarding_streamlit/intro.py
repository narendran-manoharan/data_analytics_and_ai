import streamlit as st
import numpy as np
import pandas as pd

st.write("My first streamlit")


my_list = [1, 12, 3, 5, 6, "Apples", "Eggs", "Milk"]
st.write(my_list)

my_dict = {"Col1": ["Red", "Blue", "Green", "Yellow"],
           "Col2": "colors",
           "Col3": 4,
           "Col5": "GoHome"}
st.write(my_dict)

np.random.seed(1623)
df = pd.DataFrame(data={
    "Col1": np.random.randint(10, 50, 25),
    "Col2": np.random.randint(0, 10, 25)
})
st.table(df)