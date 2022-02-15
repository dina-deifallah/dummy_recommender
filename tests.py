from recommender import recommend_random
import pandas as pd

# test recommend_random function
def test_recommender():
    movies = pd.read_csv('data/movies.csv')
    recommendations = recommend_random(movies=movies)
    assert len(recommendations)==10
