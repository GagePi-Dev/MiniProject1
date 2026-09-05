# INF 601 - Mini Project 1

A small Python client for the FHSU PracticeHub API. It authenticates with a bearer
token and wraps the posts endpoints (list, create, edit, delete) in classes.

## Setup

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root with your API token:

```
FHSU_API_TOKEN=your_token_here
```

`.env` is listed in `.gitignore` and is never committed.

## Running

```bash
python main.py
```

As written, `main.py` runs one full cycle: it lists your posts, creates a new one,
edits it, then deletes it, pausing 30 seconds after the create and the edit so you
can view the post in the browser. Every request is inside a method, so nothing hits
the API until you call it. To exercise a different endpoint, change the calls under
`if __name__ == "__main__":`

```python
print(List().posts())        # all recent posts
print(List().myPosts())      # only your posts
print(List().idPost(20))     # a single post by id

print(Create().post("My Post", "Hello world", ["python"]))

print(Edit().post(20))       # retitles post 20, returns the updated post

print(Delete().post(20))     # returns the HTTP status code
```

## Structure

| Class | Purpose |
| --- | --- |
| `PracticeHubClient` | Holds the base endpoint, the token read from `.env`, and the auth header. |
| `check()` | Wraps every request. If the response is not OK (401, 403, 404, 422, ...) it stops the script and prints the status code and the API's message. |
| `List` | `posts()`, `myPosts()`, `idPost(post_id)` - read requests. |
| `Create` | `post(title, body, tags)` - creates a post. |
| `Edit` | `post(post_id)` - retitles a post to "My Post (edited)", returns the updated post. |
| `Delete` | `post(post_id)` - deletes a post, returns the status code. |

## AI Usage

### What I used Claude Code for

Claude Code (Opus 5) wrote the error handling for this project: the `check()` helper
and the wrapping of each request in it. It also edited some of my existing functions
so they would work with that error handling. It also assisted with method handling, which is
documented in the git commit history.
Claude Code was also responsibe for the README file and more of the documentation. 

| Date | Tool | What it did |
| --- | --- | --- |
| 2026-09-05 | Claude Code (Opus 5) | Converted `List`, `Create`, and `Delete` from class attributes to methods; added parameters and a `__main__` guard. |
| 2026-09-05 | Claude Code (Opus 5) | Wrote base README. |
| 2026-09-05 | Claude Code (Opus 5) | Added the `check()` helper and wrapped each request in it. Implemented core error handling. |

### What I wrote myself

I wrote the majority of the API functions manually, based primarily on the Practice
Hub API documentation, along with calls under the `__main__` script portion that runs the
create / read / update / delete demo. I also wrote the PracticeHubClient class which was based off of the Week 2 example. 

### What I changed in AI-generated code

Most of the edits I made to the AI-written code were renaming variables and adjusting
it to be compatible with my `PracticeHubClient` class.
I also did some edits and additions to the README after Claude Code wrote the base. 