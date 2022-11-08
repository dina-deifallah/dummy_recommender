
import pandas as pd
from recommender import recommend_random

movies = pd.read_csv('data/movies.csv')
recommendations = recommend_random(movies=movies)
print(recommendations)
