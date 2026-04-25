import math
import requests

def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * radius ** 2

def circumference_of_circle(radius):
    """Calculate the circumference of a circle given its radius."""
    return 2 * math.pi * radius

radius = 5
area = area_of_circle(radius)
circumference = circumference_of_circle(radius)
print(f"Area of the circle with radius {radius}: {area:.2f}")
print(f"Circumference of the circle with radius {radius}: {circumference:.2f}")

print(math.sqrt(16))  # Output: 4.0
print(math.pow(2, 3))  # Output: 8.0

res = math.sqrt(25)
print(int(res))  # Output: 5

# Using the requests module to make an HTTP GET request
response = requests.get("https://api.github.com")
if response.status_code == 200:
    print("Request was successful!")
    print("Response content:", response.json())

