import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Read all datasets 
datasets = pd.read_csv("datasets.csv")

# Create a TFIDFVectorizer Object
tfv = TfidfVectorizer(min_df=3, max_features=None, strip_accents="unicode", analyzer="word", token_pattern=r"\w{1,}", ngram_range=(1, 3), stop_words="english")

#Filling NaNs with empty string
datasets["Overview"] = datasets["Overview"].fillna('')

# Fit the TfidfVectorizer on the "overview" text
tfv_matrix = tfv.fit_transform(datasets["Overview"])

# Calculate the cosine similarity between all dataset
cos_sim = cosine_similarity(tfv_matrix, tfv_matrix)

# Create a reverse mapping of indices
indices = pd.Series(datasets.index, index = datasets["Dataset Title"])

# Define a function to recommend dataset
def give_recommendation(title, cos_sim=cos_sim, datasets_df=datasets):
  # Get the index corresponding to the original title
  idx = indices[title]

  # Get the pairwise similarity scores
  cos_sim_scores = list(enumerate(cos_sim[idx]))
  
  # Sort the datasets
  cos_sim_scores = sorted(cos_sim_scores, key=lambda x:x[1], reverse=True)
  
  # Scores of the 10 most similar datasets
  cos_sim_scores = cos_sim_scores[0:5]

  # Datasets indices 
  dataset_indices = []
  for cos_sim_score in cos_sim_scores:
    dataset_indices.append(cos_sim_score[0])

  # Top 10 most similar datasets
  similar_datasets = datasets_df.iloc[dataset_indices]
  return similar_datasets[["id", "Dataset Title"]]


if __name__ == "__main__":
  print(give_recommendation("School District Information"))