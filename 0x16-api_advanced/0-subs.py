#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    # Define the Reddit API URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyBot/1.0'}

    try:
        # Send an HTTP GET request to the API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            # Extract the number of subscribers from the response
            subscribers_count = data['data']['subscribers']
            return subscribers_count

        # If the subreddit is invalid, Reddit may return a redirect (status code 302)
        # In that case, return 0 as specified in the requirements
        elif response.status_code == 302:
            return 0

        else:
            # Handle other possible errors here, such as 404 (Not Found)
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return 0

    except requests.exceptions.RequestException as e:
        # Handle network-related errors here
        print(f"An error occurred: {e}")
        return 0

# Example usage:
subreddit_name = "learnpython"
subscribers = number_of_subscribers(subreddit_name)
print(f"Subreddit: {subreddit_name}")
print(f"Number of Subscribers: {subscribers}")

