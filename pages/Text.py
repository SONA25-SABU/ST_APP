import streamlit as st
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load the CSV file
@st.cache_data
def load_data():
    df = pd.read_csv('CLOTH.csv')
    return df

df = load_data()

def preprocess_text(text):
    if isinstance(text, float):
        text = str(text)
    # Tokenization
    tokens = nltk.word_tokenize(text.lower())
    
    # Removing special characters and keeping only alphanumeric tokens
    tokens = [token for token in tokens if token.isalnum()]
    
    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]
    
    return tokens
    
# Apply preprocessing to the "Review Text" column
df['Preprocessed_Text'] = df['Review Text'].apply(preprocess_text)

# Display the preprocessed text
st.write("Preprocessed Text:")
st.write(df['Preprocessed_Text'])





# from sklearn.metrics import jaccard_score

# # Function to calculate Jaccard similarity
# def calculate_jaccard_similarity(text1, text2):
#     set1 = set(text1)
#     set2 = set(text2)
#     return len(set1.intersection(set2)) / len(set1.union(set2))

# # Separate the dataset into three subsets based on the "Division Name" column
# general_reviews = df[df['Division Name'] == 'General']['Preprocessed_Text']
# general_petite_reviews = df[df['Division Name'] == 'General Petite']['Preprocessed_Text']
# intimates_reviews = df[df['Division Name'] == 'Intimates']['Preprocessed_Text']

# # Preprocess text data within each subset (already preprocessed)

# # Calculate Jaccard similarity within each subset
# threshold = 0.5  # Define a threshold similarity score

# similar_reviews = []

# # For General reviews
# for i in range(len(general_reviews)):
#     for j in range(i+1, len(general_reviews)):
#         similarity_score = calculate_jaccard_similarity(general_reviews.iloc[i], general_reviews.iloc[j])
#         if similarity_score > threshold:
#             similar_reviews.append((general_reviews.index[i], general_reviews.index[j], similarity_score))

# # For General Petite reviews
# for i in range(len(general_petite_reviews)):
#     for j in range(i+1, len(general_petite_reviews)):
#         similarity_score = calculate_jaccard_similarity(general_petite_reviews.iloc[i], general_petite_reviews.iloc[j])
#         if similarity_score > threshold:
#             similar_reviews.append((general_petite_reviews.index[i], general_petite_reviews.index[j], similarity_score))

# # For Intimates reviews
# for i in range(len(intimates_reviews)):
#     for j in range(i+1, len(intimates_reviews)):
#         similarity_score = calculate_jaccard_similarity(intimates_reviews.iloc[i], intimates_reviews.iloc[j])
#         if similarity_score > threshold:
#             similar_reviews.append((intimates_reviews.index[i], intimates_reviews.index[j], similarity_score))

# # Output similar reviews
# st.write("Similar Reviews:")
# for review_pair in similar_reviews:
#     st.write(f"Review {review_pair[0]} and Review {review_pair[1]} have a Jaccard similarity score of {review_pair[2]}")





# # USING jaccard similarity implement a text similarity analysis  to identify similar reviews within the dataset for General,Generakl Petite,and Intimates from the "Division Name "column