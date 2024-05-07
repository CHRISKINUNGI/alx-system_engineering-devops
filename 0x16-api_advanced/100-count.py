#!/usr/bin/python3
"""
This module defines a recursive function that queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): Identifier for the next page of results (default None).
        counts (dict): Dictionary to store the counts of keywords (default None).

    Returns:
        None
    """
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}
    headers = {'User-Agent': 'MyBot/0.0.1'}  # Set a custom User-Agent

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            for post in posts:
                title = post['data']['title']
                for word in word_list:
                    word_lower = word.lower()
                    title_lower = title.lower()
                    if word_lower in title_lower.split():
                        counts[word_lower] = counts.get(word_lower, 0) + 1
            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, after, counts)
            else:
                sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            return
    else:
        return

# Test the function
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], sys.argv[2].split())
