import matplotlib.pyplot as plt

"""
Uses matplotlib.pyplot
This module plots the information from reddit_info as a bar graph.
"""


class plotter():

    def __init__(self, subs, appearances, time_filter):
        #self.reddit = top_sub_info(num_of_posts=400, time_filter='hour')
        self.subs = subs
        self.appearances = appearances
        self.time_filter = time_filter
        self.plot_bar_x()

    def plot_bar_x(self):
        """
        for plotting subs, appearances as bar graph
        x-axis: subreddit titles
        y-axis: number of Appearances
        """
        # for key, value in reddit.top_subs.items():
        #    subs.append(key)
        #    appearances.append(value)

        self.index = range(len(self.subs))
        plt.bar(self.index, self.appearances)
        plt.xlabel('Subreddits', fontsize=8)
        plt.ylabel('No of Appearances', fontsize=8)
        plt.xticks(self.index, self.subs, fontsize=8, rotation=30)
        plt.title(
            'Subreddits most frequently appearing in r/all. Filter: ' + self.time_filter)
        plt.show()
