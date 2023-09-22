import pandas as pd
import numpy as np

# Read all movies using pandas
movies = pd.read_csv("output.csv")

from sklearn.feature_extraction.text import TfidfVectorizer
tfv = TfidfVectorizer(min_df=3, max_features=None,
                     strip_accents="unicode", analyzer="word", token_pattern=r"\w{1,}",
                     ngram_range=(1, 3), stop_words="english")

movies["Overview"] = movies["Overview"].fillna("")

# Fitting the TF-IDF on the "Overview" text
tfv_matrix = tfv.fit_transform(movies["Overview"])

from sklearn.metrics.pairwise import cosine_similarity

# Compute the cosine similarity kernel
cos_sim = cosine_similarity(tfv_matrix, tfv_matrix)

# Reverse mapping of indices
indices = pd.Series(movies.index, index=movies["Dataset Title"]).drop_duplicates()

def give_rec(title, cos_sim=cos_sim, movies_df=movies):
    # Get the index corresponding to the original title
    idx = indices[title]
    
    # Get the pairwise similarity scores
    cos_sim_scores = list(enumerate(cos_sim[idx]))
    
    # Sort the movies
    cos_sim_scores = sorted(cos_sim_scores, key=lambda x: x[1], reverse=True)
    
    # Scores of the 10 most similar movies
    cos_sim_scores = cos_sim_scores[0:11]
    
    # Movies indices
    movie_indices = [i[0] for i in cos_sim_scores]
    print("Dataset indices", movie_indices)
    
    # Top 10 most similar movies
    similar_movies = movies_df.iloc[movie_indices]
    return similar_movies[["id", "Dataset Title"]]

print(give_rec("School District Information"))
