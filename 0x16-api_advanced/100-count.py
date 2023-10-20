#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, after=None, word_count=None):
    # Initialize word_count as an empty dictionary on the first call
    if word_count is None:
        word_count = {}

    # Base case: If after is None, print the sorted count of keywords
    if after is None:
        sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0].lower()))
        for keyword, count in sorted_counts:
            print(f"{keyword.lower()}: {count}")
        return

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

            # Extract and parse the titles of hot posts
            for post in children:
                title = post['data']['title']
                for word in title.split():
                    # Check if the word is in the word_list
                    keyword = word.lower()
                    if keyword in word_list:
                        if keyword not in word_count:
                            word_count[keyword] = 1
                        else:
                            word_count[keyword] += 1

            # Get the 'after' value for the next page
            after = data['data']['after']

            # Recursively call the function for the next page
            return count_words(subreddit, word_list, after, word_count)

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
keyword_list = ["python", "java"]
print(f"Keyword counts in subreddit: {subreddit_name}")
count_words(subreddit_name, keyword_list)

