import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.header("The Best Company")
st.write("Some Text")

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)
dt1 = pandas.read_csv(r"D:\Udemy_Courses\Pyhton\Udemy\Python Mega Course by Ardit Sulce\Section-22-Practice-code\data.csv")
# dt2 = pandas.read_csv('topics.csv', sep="")

with col1:
    for index, row in dt1[:4].iterrows():
        st.header(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"])
        st.image(r"D:\Udemy_Courses\Pyhton\Udemy\Python Mega Course by Ardit Sulce\Section-22-Practice-code\images/" + row["image"])

with col2:
    for index, row in dt1[4:8].iterrows():
        st.header(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"])
        st.image(r"D:\Udemy_Courses\Pyhton\Udemy\Python Mega Course by Ardit Sulce\Section-22-Practice-code\images/" + row["image"])

with col3:
    for index, row in dt1[8:12].iterrows():
        st.header(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row["role"])
        st.image(r"D:\Udemy_Courses\Pyhton\Udemy\Python Mega Course by Ardit Sulce\Section-22-Practice-code\images/" + row["image"])