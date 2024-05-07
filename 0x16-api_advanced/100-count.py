#!/usr/bin/python3
"""
Recursively queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): Parameter for pagination, indicating the post after which to start the next page.
        counts (dict): Dictionary to store counts of keywords.

    Returns:
        None
    """
    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit, after)
    
    headers = {'User-Agent': 'MyBot/0.0.1'}  # Set a custom User-Agent
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if title.count(word.lower()) > 0:
                    if word.lower() in counts:
                        counts[word.lower()] += title.count(word.lower())
                    else:
                        counts[word.lower()] = title.count(word.lower())
        after = data['data']['after']
        if after is not None:
            return count_words(subreddit, word_list, after, counts)
        else:
            for word in sorted(counts.keys(), key=lambda x: (-counts[x], x)):
                print("{}: {}".format(word, counts[word]))
    else:
        print(None)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])

