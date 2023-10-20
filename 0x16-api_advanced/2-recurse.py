#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=None, after=None):
    # Initialize hot_list as an empty list on the first call
    if hot_list is None:
        hot_list = []

    # Base case: If after is None, return the hot_list
    if after is None:
        return hot_list

    # Define the Reddit API URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    # Set a custom User-Agent to avoid potential issues
    headers = {'User-Agent': 'MyBot/1.0'}

    try:
        # Include the 'after' parameter for pagination
        if after:
            url += f'&after={after}'

        # Send an HTTP GET request to the API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            children = data['data']['children']

            # Extract and add the titles of hot posts to the list
            for post in children:
                hot_list.append(post['data']['title'])

            # Get the 'after' value for the next page
            after = data['data']['after']

            # Recursively call the function for the next page
            return recurse(subreddit, hot_list, after)

        # If the subreddit is invalid, Reddit may return a redirect (status code 302)
        # In that case, return None as specified in the requirements
        elif response.status_code == 302:
            return None

        else:
            # Handle other possible errors here, such as 404 (Not Found)
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        # Handle network-related errors here
        print(f"An error occurred: {e}")
        return None

# Example usage:
subreddit_name = "learnpython"
print(f"Hot articles in subreddit: {subreddit_name}")
hot_articles = recurse(subreddit_name)

if hot_articles is not None:
    for i, title in enumerate(hot_articles, start=1):
        print(f"{i}. {title}")
else:
    print("Invalid subreddit or no results found.")

