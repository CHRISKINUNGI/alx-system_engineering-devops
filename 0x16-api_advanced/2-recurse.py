#!/usr/bin/python3
"""
This module defines a recursive function that queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively retrieves all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List containing titles of hot articles (default None).
        after (str): Identifier for the next page of results (default None).

    Returns:
        list or None: List containing titles of hot articles, or None if no results found.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}
    headers = {'User-Agent': 'MyBot/0.0.1'}  # Set a custom User-Agent

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    else:
        return None

# Test the function
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
