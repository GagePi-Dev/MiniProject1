# INF601 - Advanced Programming in Python
# Gage Giffin
# Mini Project 1

# Imports (Requirement #2)
import os
import requests
from dotenv import load_dotenv
from time import sleep

# Load API Token
load_dotenv()  # reads FHSU_API_TOKEN from the .env file

# API Header (Requirement #3)
class PracticeHubClient:
    ENDPOINT = "https://practice.fhsucyber.com"
    TOKEN = os.environ.get("FHSU_API_TOKEN")
    HEADERS = {"Authorization": f"Bearer {TOKEN}"}

# Error Handling
def check(resp):
    if not resp.ok:
        detail = resp.json()["detail"]
        if isinstance(detail, list):
            detail = detail[0]["msg"]  # 422 sends a list of validation errors
        raise SystemExit(f"Error {resp.status_code}: {detail}")
    return resp

# Create A Post (Requirement #4)
class Create:
    def post(self, title, body, tags):
        return check(requests.post(
            f"{PracticeHubClient.ENDPOINT}/api/v1/posts",
            headers=PracticeHubClient.HEADERS,
            json={
                "title": title,
                "body": body,
                "tags": tags,
                },
            )).json()

# List Posts (Requirement #5)
class List:
    def posts(self):
        return check(requests.get(
            f"{PracticeHubClient.ENDPOINT}/api/v1/posts",
            headers=PracticeHubClient.HEADERS,
            )).json()

    def myPosts(self):
        return check(requests.get(
            f"{PracticeHubClient.ENDPOINT}/api/v1/posts",
            headers=PracticeHubClient.HEADERS,
            params={"mine": True},
            )).json()

    def idPost(self, post_id):
        return check(requests.get(
            f"{PracticeHubClient.ENDPOINT}/api/v1/posts/{post_id}",
            headers=PracticeHubClient.HEADERS,
            )).json()

# Edit A Post (Requirement #6)
class Edit:
    def post(self, post_id):
        return check(requests.patch(
            f"{PracticeHubClient.ENDPOINT}/api/v1/posts/{post_id}",
            headers=PracticeHubClient.HEADERS,
            json={"title": "My Post (edited)"},
            )).json()

# Delete A Post (Requirement #7)
class Delete:
    def post(self, post_id):
        resp = check(requests.delete(
            f"{PracticeHubClient.ENDPOINT}/api/v1/posts/{post_id}",
            headers=PracticeHubClient.HEADERS,
            ))
        return resp.status_code

# Only the calls below actually hit the API (Requirement #9)
if __name__ == "__main__":
    print("\n\nPosts BEFORE Script\n---------------")
    print(List().myPosts())

    print("\n\nCreate A Post\n---------------")
    newPost = Create().post("My Post Cycle", "Hello From My Python Script", ["python"])
    newPostId = newPost["id"]
    print(List().idPost(newPostId))
    print("\nYou have 30 seconds to view on https://practice.fhsucyber.com/ before continuing.")
    sleep(30)

    print("\n\nEdit A Post\n---------------")
    Edit().post(newPostId)
    print(List().idPost(newPostId))
    print("\nYou have 30 seconds to view on https://practice.fhsucyber.com/ before continuing.")
    sleep(30)

    print("\n\nDelete A Post\n---------------")
    status = Delete().post(newPostId)
    if status == 204:
        print("Delete was successful.")
    else:
        print(f"Error: Code {status}")