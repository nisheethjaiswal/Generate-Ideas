import streamlit as st
import pandas as pd
import random

st.title('Generating ideas using random combinations')


trends_list = pd.read_excel("Innovation gen.xlsx", sheet_name='Trends', header=None)

sayings_list = pd.read_excel("Innovation gen.xlsx", sheet_name='Sayings', header=None)

skills_interests_list = pd.read_excel("Innovation gen.xlsx", sheet_name='Skills&Interests', header=None)

col1, col2, col3 = st.columns(3)
with col1: 
    st.header("Trends")
    st.write(trends_list)

with col2:
    st.header("Sayings")
    st.write(sayings_list)
    
with col3:
    st.header("Skills/Interests")
    st.write(skills_interests_list)


rand_trend = str(trends_list.sample(1))
rand_saying = str(sayings_list.sample(1))
rand_skill = str(skills_interests_list.sample(1))

st.header("Combination from above list of ideas")
st.write(rand_trend)
st.write(rand_saying)
st.write(rand_skill)