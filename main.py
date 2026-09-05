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

# Create A Post (Requirement #4)
class Create:
    def newPost(self, title, body, tags):
        return requests.post(
            f"{PracticeHubClient.ENDPOINT}/api/v1/posts",
            headers=PracticeHubClient.HEADERS,
            json={
                "title": title,
                "body": body,
                "tags": tags,
                },
            ).json()

# List Posts (Requirement #5)
class List:
    def posts(self):
        return requests.get(
            f"{PracticeHubClient.ENDPOINT}/api/v1/posts",
            headers=PracticeHubClient.HEADERS,
            ).json()

    def myPosts(self):
        return requests.get(
            f"{PracticeHubClient.ENDPOINT}/api/v1/posts",
            headers=PracticeHubClient.HEADERS,
            params={"mine": True},
            ).json()

    def idPost(self, post_id):
        return requests.get(
            f"{PracticeHubClient.ENDPOINT}/api/v1/posts/{post_id}",
            headers=PracticeHubClient.HEADERS,
            ).json()

# Edit A Post (Requirement #6)
class Edit:
    def edit(self, post_id):
        resp = requests.patch(
            f"{PracticeHubClient.ENDPOINT}/api/v1/posts/{post_id}",
            headers=PracticeHubClient.HEADERS,
            json={"title": "My Post (edited)"},
            ).json()

# Delete A Post (Requirement #7)
class Delete:
    def post(self, post_id):
        resp = requests.delete(
            f"{PracticeHubClient.ENDPOINT}/api/v1/posts/{post_id}",
            headers=PracticeHubClient.HEADERS,
            )
        return resp.status_code

# Only the calls below actually hit the API
if __name__ == "__main__":
    print(List().myPosts())
