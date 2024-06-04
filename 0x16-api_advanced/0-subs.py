#!/usr/bin/python3
""" Function that queries the Reddit API and returns the number of active
subscribers. Returns 0 if the function should return 0."""

import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0