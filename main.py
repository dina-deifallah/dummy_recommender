'''
main program for dummy recommender
'''

import pandas as pd
from recommender import recommend_random



movies = pd.read_csv('data/movies.csv')
recommendations = recommend_random(movies=movies)
assert len(recommendations)==10
  print(recommendations)
