# Reddit API Project

## Overview

This project aims to enhance understanding and proficiency in utilizing APIs, specifically focusing on the Reddit API. It includes implementations of functions to interact with the Reddit API, such as retrieving the number of subscribers, fetching the top posts, and recursively retrieving all hot articles for a given subreddit.

## Requirements

### General

- Allowed editors: vi, vim, emacs
- Interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Libraries imported in Python files must be organized in alphabetical order
- A README.md file, at the root of the folder of the project, is mandatory
- Code should adhere to PEP 8 style
- All files must be executable
- The length of files will be tested using wc
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Requests module must be used for sending HTTP requests to the Reddit API

### Tasks

1. **How many subs?**
    - Write a function that queries the Reddit API and returns the number of subscribers for a given subreddit.

2. **Top Ten**
    - Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

3. **Recurse it!**
    - Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

## Usage

Each task is implemented in a separate Python file within the project directory. The main scripts (e.g., `0-main.py`, `1-main.py`, `2-main.py`) demonstrate the usage of these functions with example inputs.

To execute a specific task, run the corresponding main script followed by the subreddit name as a command-line argument.

Example:
