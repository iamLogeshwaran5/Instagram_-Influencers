import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the cleaned dataset
@st.cache
def load_data():
    data = pd.read_csv('C:/Users/wolfr/OneDrive/Desktop/Logeshwaran_WorkSpace/Instagram_Influencer/Cleaned_Influencer_Data.csv')
    return data

data = load_data()

# Add Instagram logo icon
st.image("https://th.bing.com/th/id/OIP.mdNMeNAxQL1gWv0U3KAe1gHaHZ?rs=1&pid=ImgDetMain", width=100)  

# Define the title of the app
title = "Instagram Influence Data Analysis Insight"

# Display the title at the top of the page
st.title(title)

# Add creator information
st.markdown("Created by **Logeshwaran**")
st.markdown("[logeshwaran1478@gmail.com](mailto:logeshwaran1478@gmail.com)")

# Add LinkedIn link icon button
st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/your_link_here)")

# Add professional background with multicolor gradient effect
st.markdown(
    """
    <style>
    .background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        background: linear-gradient(135deg, #FF5733, #FFC300, #DAF7A6, #C70039);
    }
    </style>
    <div class="background"></div>
    """,
    unsafe_allow_html=True
)

# Displaying the correlation matrix
st.header("Correlation Matrix")
numeric_data = data.select_dtypes(include=['number'])  # Ensure only numeric data is used
correlation_matrix = numeric_data.corr()
st.write(correlation_matrix)

# Plotting function to reuse
def plot_data(column, title):
    fig, ax = plt.subplots()
    sns.countplot(x=column, data=data)
    plt.title(title)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Frequency Distributions
st.header("Frequency Distributions")
cols = ['Influence Score', 'Followers', 'Posts']
for col in cols:
    plot_data(col, f'Frequency Distribution of {col}')

# Count of Instagram Influencers by Country
st.header("Count of Instagram Influencers by Country")
fig, ax = plt.subplots()
sns.countplot(y='Country Or Region', data=data, order=data['Country Or Region'].value_counts().index)
plt.title('Instagram Influencers by Country')
st.pyplot(fig)

# Top 10 influencers
st.header("Top 10 Influencers")
features = ['Followers', 'Avg. Likes', 'Total Likes']
for feature in features:
    st.subheader(f"Top 10 Based on {feature}")
    top_infs = data.sort_values(by=feature, ascending=False).head(10)
    st.write(top_infs[['Channel Info', feature]])

# Relationships between features
st.header("Relationships Between Features")
pairs = [
    ('Followers', 'Total Likes'),
    ('Followers', 'Influence Score'),
    ('Posts', 'Avg. Likes'),
    ('Posts', 'Influence Score')
]

for x, y in pairs:
    fig, ax = plt.subplots()
    sns.scatterplot(x=x, y=y, data=data)
    plt.title(f'Relationship between {x} and {y}')
    st.pyplot(fig)
