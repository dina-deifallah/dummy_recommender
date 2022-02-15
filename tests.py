"module containing all tests on my recommender"

import pandas as pd
from recommender import recommend_random

# test recommend_random function
def test_recommender():
    "testing that my recommender returns the default k recommendations"
    movies = pd.read_csv('data/movies.csv')
    recommendations = recommend_random(movies=movies)
    assert len(recommendations)==10
