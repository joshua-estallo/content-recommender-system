import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec

# Read all datasets
datasets = pd.read_csv("datasets.csv")

# Create a Word2Vec model
w2v_model = Word2Vec.load("word2vec_model.bin")

# Generate word embeddings for the dataset
dataset_embeddings = []
for dataset in datasets:
    dataset_embedding = np.zeros(w2v_model.vector_size)
    for word in dataset["Overview"]:
        if word in w2v_model.wv:
            dataset_embedding += w2v_model.wv[word]
    dataset_embeddings.append(dataset_embedding)

# Calculate the cosine similarity between all dataset
cos_sim = cosine_similarity(dataset_embeddings, dataset_embeddings)

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
