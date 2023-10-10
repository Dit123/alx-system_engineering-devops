#!/usr/bin/python3

import requests

def top_ten(subreddit):
    # Define the Reddit API URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid potential issues
    headers = {'User-Agent': 'MyBot/1.0'}

    try:
        # Send an HTTP GET request to the API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            # Extract and print the titles of the first 10 hot posts
            for post in data['data']['children']:
                print(post['data']['title'])

        # If the subreddit is invalid, Reddit may return a redirect (status code 302)
        # In that case, print None as specified in the requirements
        elif response.status_code == 302:
            print("None")

        else:
            # Handle other possible errors here, such as 404 (Not Found)
            print(f"Failed to retrieve data. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Handle network-related errors here
        print(f"An error occurred: {e}")

# Example usage:
subreddit_name = "learnpython"
print(f"Top 10 hot posts in subreddit: {subreddit_name}")
top_ten(subreddit_name)

