# import packages
import pandas as pd
import matplotlib.pyplot as plt 
import streamlit as  st

plt.style.use('seaborn-v0_8')
# show the title
st.title('Titanic App by Hairong Zheng')

# read csv and show the dataframe
df=pd.read_csv('train.csv')

st.write(df)
# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

fig, ax = plt.subplots(1, 3, figsize=(15, 5))
df[df.Pclass==1].boxplot(column='Fare',ax=ax[0])
ax[0].set_xlabel('Pclass=1')
ax[0].set_ylabel('Fare')
df[df.Pclass==2].boxplot(column='Fare',ax=ax[1])
ax[1].set_xlabel('Pclass=2')
df[df.Pclass==3].boxplot(column='Fare',ax=ax[2])
ax[2].set_xlabel('Pclass=3')
st.pyplot(fig)
