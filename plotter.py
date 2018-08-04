import matplotlib.pyplot as plt
from reddit_info import top_sub_info

reddit = top_sub_info(num_of_posts=400, time_filter='hour')
subs = []
appearances = []

def plot_bar_x():
    """
    for plotting top_sub_info.top_subs as bar graph
    x-axis: subreddit titles
    y-axis: number of Appearances
    """
    for key, value in reddit.top_subs.items():
        subs.append(key)
        appearances.append(value)

    index = range(len(subs))
    plt.bar(index, appearances)
    plt.xlabel('Subreddits', fontsize=8)
    plt.ylabel('No of Appearances', fontsize=8)
    plt.xticks(index, subs, fontsize=8, rotation=30)
    plt.title('Subreddits most frequently appearing in r/all. Filter: ' + reddit.time_filter)
    plt.show()

plot_bar_x()
