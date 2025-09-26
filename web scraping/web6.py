import requests
import re
import os
import json

searchQuery = input("Enter the image name: ")

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

url = f"https://www.google.com/search?sxsrf=AE3TifNMfoVCTwH-2wdfzXEyglkzF6dYeQ:1758714084286&udm=2&q={searchQuery}"

response = requests.get(url=url, headers=user_agent).text

pattern = r'\["(https://[^"]+\.jpg)",\d+,\d+\]'
images = re.findall(pattern, response)

print(f"Total Images Found: {len(images)}")

if not images:
    print("No images found.")
    exit()

max_images = len(images)
no_of_images = int(input(f"Enter number of images to download (max {max_images}): "))
no_of_images = min(no_of_images, max_images)

if not os.path.exists("images"):
    os.makedirs("images")

os.chdir("images")

for idx, image_url in enumerate(images[:no_of_images]):
    try:
        print(f"Downloading Image {idx+1}: {image_url}")
        image_data = requests.get(url=image_url, headers=user_agent).content
        with open(f"image_{idx+1}.jpg", "wb") as f:
            f.write(image_data)
    except Exception as e:
        print(f"Error downloading image {idx+1}: {e}")
