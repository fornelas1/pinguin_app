import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

image= Image.open('Penguin-clipart.png')
image = image.resize((100, 100))
st.image(image,caption= 'Baby Penguin')

st.title("Palmer's Penguins")
st.markdown('Use this app to make scatter plots on penguins')

penguin_file = st.file_uploader('Select Your Local Penguins CSV file (default provided)')

# @st.cache - prevents streamlit from running same proc
@st.cache()
def load_file(penguin_file):
    if penguin_file is not None:
        df = pd.read_csv(penguin_file)
    else:
        df = pd.read_csv(r'pinguin_data.csv')
    return(df)

pinguins_df= load_file(penguin_file)    

selected_species= st.selectbox('Chose a specie to visualize', ['Adelie', 'Gentoo', 'Chinstrap'])

selected_xvar= st.selectbox('What is the X variable you want to plot?',['bill_length_mm','bill_depth_mm','filpper_length_mm','body_mass_g'])

selected_yvar= st.selectbox('What is your y?',['bill_depth_mm', 'bill_length_mm','flipper_length_mm','body_mass_g'])

selected_gender= st.selectbox('Filtering for Gender, make a choice', ['all penguins', 'female', 'male'])

#if selected_species== 'Adelie':
#    pinguins_df= pinguins_df[pinguins_df['species']=='Adelie']
#elif selected_species== 'Gentoo':
#    pinguins_df= pinguins_df[pinguins_df['species']=='Gentoo']
#elif selected_species=='Chinstrap':
#    pinguins_df= pinguins_df[pinguins_df['species']=='Chinstrap']   
#else:
#    pass    

if selected_gender== 'male':
    pinguins_df= pinguins_df[pinguins_df['sex']=='male']
elif selected_gender== 'female':
    pinguins_df= pinguins_df[pinguins_df['sex']=='female']
else:
    pass    
#import the data
#pinguins_df= pd.read_csv(r'pinguin_data.csv')
st.write(pinguins_df.head())

st.write(pinguins_df.info())

fig, ax = plt.subplots()
ax = sns.scatterplot(x = pinguins_df[selected_xvar],
y = pinguins_df[selected_yvar])
plt.xlabel(selected_xvar)
plt.ylabel(selected_yvar)
plt.title('Scatterplot for {} Penguins'.format(selected_species))
st.pyplot(fig)


sns.set_style('darkgrid')
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
fig, ax = plt.subplots()
ax = sns.scatterplot(data = pinguins_df, x = selected_xvar,
y = selected_yvar, hue = 'species', markers = markers,
style = 'species')
plt.xlabel(selected_xvar)
plt.ylabel(selected_yvar)
plt.title("Scatterplot of Palmer's Penguins: {}")
st.pyplot(fig)
#Note: The code above is not in the correct format, please fix it

