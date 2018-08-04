from reddit_info import top_sub_info
from plotter import plotter

NUM_OF_POSTS = 400
TIME_FILTER = 'all'

reddit = top_sub_info(NUM_OF_POSTS, TIME_FILTER)
subs = []
appearances = []

for key, value in reddit.top_subs.items():
    subs.append(key)
    appearances.append(value)

abc = plotter(subs, appearances, reddit.time_filter)
