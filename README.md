# INF 601 - Mini Project 1

A small Python client for the FHSU PracticeHub API. It authenticates with a bearer
token and wraps the posts endpoints (list, list-mine, get-by-id, create, delete)
in classes.

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

As written, `main.py` prints your own posts. Every request is inside a method, so
nothing hits the API until you call it. To exercise a different endpoint, change
the calls under `if __name__ == "__main__":`

```python
lister = List()
print(lister.posts())        # all recent posts
print(lister.myPosts())      # only your posts
print(lister.idPost(20))     # a single post by id

creator = Create()
print(creator.newPost("My Post", "Hello world", ["python"]))

deleter = Delete()
print(deleter.post(20))      # returns the HTTP status code
```

## Structure

| Class | Purpose |
| --- | --- |
| `PracticeHubClient` | Holds the base endpoint, the token read from `.env`, and the auth header. |
| `List` | `posts()`, `myPosts()`, `idPost(post_id)` - read requests. |
| `Create` | `newPost(title, body, tags)` - creates a post. |
| `Delete` | `post(post_id)` - deletes a post, returns the status code. |

## AI Usage

| Date | Tool | What it did |
| --- | --- | --- |
| 2026-09-05 | Claude Code (Opus 5) | Converted `List`, `Create`, and `Delete` from class attributes to methods; added parameters and a `__main__` guard. |
| 2026-09-05 | Claude Code (Opus 5) | Wrote base README. |
