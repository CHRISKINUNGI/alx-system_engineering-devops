#!/usr/bin/python3


"""
This module queries the Reddit API and returns the
number of subscribers for a given subreddit.
"""


import requests
import sys


def number_of_subscribers(subreddit):

    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0


def main():

    """
    Main function to handle command-line arguments and call
    the number_of_subscribers function.
    """
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print(number_of_subscribers(subreddit))


if __name__ == "__main__":
    main()
