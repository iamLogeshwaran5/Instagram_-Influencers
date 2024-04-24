# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# %% [markdown]
# # Load the dataset

# %%
file_path = 'C:/Users/wolfr/OneDrive/Desktop/Logeshwaran_WorkSpace/Instagram_Influencer/Influencer.csv'
data = pd.read_csv(file_path)

# %% [markdown]
# # Function to remove unwanted symbols

# %%
# Function to remove unwanted symbols
def clean_symbols(text):
    return text.replace('/', '').replace('\\', '').strip()

# %% [markdown]
# # Function to convert shorthand notations like 'm', 'k', and 'b' to full numerical values
# 

# %%
def shorthand_to_number(value):
    if 'b' in value:
        return float(value.replace('b', '')) * 1_000_000_000
    elif 'm' in value:
        return float(value.replace('m', '')) * 1_000_000
    elif 'k' in value:
        return float(value.replace('k', '')) * 1_000
    else:
        try:
            return float(value)
        except ValueError:
            return None  # Return None if conversion is not possible

# %% [markdown]
# # Applying cleaning functions to relevant columns

# %%
data['Channel Info'] = data['Channel Info'].apply(clean_symbols)
data['Followers'] = data['Followers'].apply(shorthand_to_number)
data['Total Likes'] = data['Total Likes'].apply(shorthand_to_number)
data['New Post Avg. Likes'] = data['New Post Avg. Likes'].apply(shorthand_to_number)
data['Avg. Likes'] = data['Avg. Likes'].apply(shorthand_to_number)
data['Posts'] = data['Posts'].apply(shorthand_to_number)

# %% [markdown]
# # Remove rows where 'Country Or Region' is blank
# 

# %%
data.dropna(subset=['Country Or Region'], inplace=True)

# %% [markdown]
# # Save the cleaned dataset to a new CSV file

# %%
cleaned_file_path = 'C:/Users/wolfr/OneDrive/Desktop/Logeshwaran_WorkSpace/Instagram_Influencer/Cleaned_Influencer_Data.csv'

data.to_csv(cleaned_file_path, index=False)
print("Data cleaned and saved successfully.")

# %% [markdown]
# # Reload the cleaned data for analysis

# %%
data = pd.read_csv(cleaned_file_path)

# %% [markdown]
# # 1. Check for correlated features
# # Filter out non-numeric data before computing the correlation matrix

# %%
numeric_data = data.select_dtypes(include=[np.number])  # Only include numeric columns
correlation_matrix = numeric_data.corr()
print("Correlation matrix:\n", correlation_matrix)

# %% [markdown]
# # Find the highest correlated pairs (excluding self-correlation of 1)

# %%
sorted_pairs = correlation_matrix.unstack().sort_values(kind="quicksort", ascending=False)
strong_pairs = sorted_pairs[(sorted_pairs < 1) & (sorted_pairs > 0.5)]
print("Highly correlated pairs:\n", strong_pairs)

# %% [markdown]
# # 2. Frequency distribution of specified features

# %%
def plot_distribution(column, title):
    plt.figure(figsize=(10, 6))
    sns.countplot(x=column, data=data)
    plt.title(f'Frequency Distribution of {title}')
    plt.xticks(rotation=45)
    plt.show()

# %%
plot_distribution('Influence Score', 'Influence Score')
plot_distribution('Followers', 'Followers')
plot_distribution('Posts', 'Posts')

# %% [markdown]
# # 3. Which country houses the highest number of Instagram Influencers?

# %%
plt.figure(figsize=(12, 8))
sns.countplot(y='Country Or Region', data=data, order=data['Country Or Region'].value_counts().index)
plt.title('Count of Instagram Influencers by Country')
plt.xlabel('Count')
plt.ylabel('Country')
plt.show()

# %% [markdown]
# # 4. Top 10 influencers based on various features

# %%
def top_influencers(feature, n=10):
    top_infs = data.sort_values(by=feature, ascending=False).head(n)
    print(f"Top 10 influencers based on {feature}:\n", top_infs[['Channel Info', feature]])

top_influencers('Followers')
top_influencers('Avg. Likes')
top_influencers('Total Likes')

# %% [markdown]
# # 5. Relationship between pairs of features

# %%
def plot_relationship(x, y):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x, y=y, data=data)
    plt.title(f'Relationship between {x} and {y}')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()

# %%
plot_relationship('Followers', 'Total Likes')
plot_relationship('Followers', 'Influence Score')
plot_relationship('Posts', 'Avg. Likes')
plot_relationship('Posts', 'Influence Score')


