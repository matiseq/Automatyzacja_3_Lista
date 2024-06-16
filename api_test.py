import requests
import json

def send_request(url):
    response = requests.get(url)
    return response.status_code, response.json()

def check_status(http_code):
    return http_code == 200

def check_json_keys(json_data, keys):
    for key in keys:
        if key not in json_data:
            return False
    return True

def test_endpoint(url, keys):
    http_code, json_data = send_request(url)
    if not check_status(http_code):
        return "FAILED"
    if check_json_keys(json_data, keys):
        return "PASSED"
    else:
        return "FAILED"

# Testowanie endpointów
tests = [
    ("https://jsonplaceholder.typicode.com/posts/1", ["userId", "id", "title", "body"]),
    ("https://jsonplaceholder.typicode.com/users/1", ["id", "name", "username", "email"]),
    ("https://jsonplaceholder.typicode.com/comments/1", ["postId", "id", "name", "email", "body"])
]

for i, (url, keys) in enumerate(tests, 1):
    result = test_endpoint(url, keys)
    print(f"Test {i}: {result}")
