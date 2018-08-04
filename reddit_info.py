import praw

class top_sub_info():
    def __init__(self, num_of_posts, time_filter):
        """
        variables:-
            num_of_posts : number of top posts to input
            time_filter : time filter to apply; 'all', 'year', 'month', 'week', 'day', 'hour'
            top_subs : subs with more appearances than num_of_posts/30
            all_subs : all subs appearing in top num_of_posts with time_filter

        sets up reddit variable with client_id, client_secret, and user_agent
        calls get_info()
        """
        self.reddit = praw.Reddit(client_id='meg3AXo1h_gZ8Q',
                                  client_secret='7Pxe3orRCXswMlSX49-p9lqot68',
                                  user_agent='Reddit Top Subs v1.0 by /u/aryan096 www.github.com/aryan096')
        self.num_of_posts = num_of_posts
        self.time_filter = time_filter
        self.top_subs = {}
        self.all_subs = {}
        self.get_info()


    def get_info(self):
        """
        for each top num_of_posts submissions in r/all with time_filter,
        calculates number of appearances of each subreddit
        adds Subreddits appearing more than num_of_posts/30 times to top_subs
        """
        for submission in self.reddit.subreddit('all').top(time_filter=self.time_filter, limit=self.num_of_posts):
            if submission.subreddit.display_name in self.all_subs.keys():
                self.all_subs[submission.subreddit.display_name] += 1
            else:
                self.all_subs[submission.subreddit.display_name] = 1

        for key, value in self.all_subs.items():
            if value > self.num_of_posts/30:
                self.top_subs[key] = value
