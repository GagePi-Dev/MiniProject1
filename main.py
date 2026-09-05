# INF601 - Advanced Programming in Python
# Your Name
# Mini Project 1

# Imports
import os
import requests
from dotenv import load_dotenv

# Load API Token
load_dotenv()  # reads FHSU_API_TOKEN from the .env file

# Variables
BASE = "https://practice.fhsucyber.com"
TOKEN = os.environ.get("FHSU_API_TOKEN")
headers = {"Authorization": f"Bearer {TOKEN}"}

# Who am I?
print(requests.get(f"{BASE}/api/v1/me", headers=headers).json())

# Read recent posts
print(requests.get(f"{BASE}/api/v1/posts", headers=headers).json())

# Generate some practice data (no public API needed)
print(requests.get(f"{BASE}/api/v1/datasets/people",
                   headers=headers, params={"count": 5}).json())
