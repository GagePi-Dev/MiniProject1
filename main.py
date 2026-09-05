# INF601 - Advanced Programming in Python
# Your Name
# Mini Project 1

# Imports (Requirement #2)
import os
import requests
from dotenv import load_dotenv

# Load API Token
load_dotenv()  # reads FHSU_API_TOKEN from the .env file

# API Header (Requirement #3)
class PracticeHubClient:
    ENDPOINT = "https://practice.fhsucyber.com"
    TOKEN = os.environ.get("FHSU_API_TOKEN")
    HEADERS = {"Authorization": f"Bearer {TOKEN}"}

# List Posts
posts = requests.get(
    f"{PracticeHubClient.ENDPOINT}/api/v1/posts",
    headers=PracticeHubClient.HEADERS,
    ).json()

my_posts = requests.get(
    f"{PracticeHubClient.ENDPOINT}/api/v1/posts",
    headers=PracticeHubClient.HEADERS,
    params={"mine": True},
    ).json()

# Create A Post (Requirement #4)
new_post = requests.post(f"{PracticeHubClient.ENDPOINT}/api/v1/posts", headers=PracticeHubClient.HEADERS, json={
    "title": "My Post",
    "body": "Hello world",
    "tags": ["python"],
    }).json()
post_id = new_post["id"]

print(posts)

# Who am I?
#print(requests.get(f"{BASE}/api/v1/me", headers=headers).json())

# Read recent posts
#print(requests.get(f"{BASE}/api/v1/posts", headers=headers).json())

# Generate some practice data (no public API needed)
#print(requests.get(f"{BASE}/api/v1/datasets/people",
#                   headers=headers, params={"count": 5}).json())
