import requests

# Make a GET request to a URL
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.json())

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("Request successful.")
    print("Title: " + data["title"])
    print("Body: " + data["body"])
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")

# Make a POST request to a URL
post_url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "foo",
    "body": "bar",
    "userId": 100001
}
post_response = requests.post(post_url, json=payload)
if post_response.status_code == 201:
    print("POST request successful.")
    print(post_response.json())
else:
    print(f"POST request failed with status code: {post_response.status_code}")
    
#Get request with query parameters
query_url = "https://jsonplaceholder.typicode.com/posts/1"
query_response = requests.get(query_url)
if query_response.status_code == 200:
    print("GET request with query parameters successful.")
    print(query_response.json())
else:
    print(f"GET request with query parameters failed with status code: {query_response.status_code}")
    
# get all posts
# all_posts_url = "https://jsonplaceholder.typicode.com/posts"
# all_posts_response = requests.get(all_posts_url)
# if all_posts_response.status_code == 200:
#     print("GET request for all posts successful.")
#     print(all_posts_response.json())
# else:
#     print(f"GET request for all posts failed with status code: {all_posts_response.status_code}")
    
#Make a PUT request to update a post
put_url = "https://jsonplaceholder.typicode.com/posts/1"
put_payload = {
    "id": 1,
    "title": "updated title",
    "body": "updated body",
    "userId": 100001
}
put_response = requests.put(put_url, json=put_payload)
if put_response.status_code == 200:
    print("PUT request successful.")
    print(put_response.json())
else:
    print(f"PUT request failed with status code: {put_response.status_code}")     
    
#Make a DELETE request to delete a post
delete_url = "https://jsonplaceholder.typicode.com/posts/1"
delete_response = requests.delete(delete_url)
if delete_response.status_code == 200:
    print("DELETE request successful.")
else:
    print(f"DELETE request failed with status code: {delete_response.status_code}")
    
#Make a PATCH request to partially update a post
patch_url = "https://jsonplaceholder.typicode.com/posts/1"
patch_payload = {
    "title": "partially updated title"
}
patch_response = requests.patch(patch_url, json=patch_payload)
if patch_response.status_code == 200:
    print("PATCH request successful.")
    print(patch_response.json())
else:
    print(f"PATCH request failed with status code: {patch_response.status_code}")   