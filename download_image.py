import requests

def download_image(url, filename):
  """Downloads an image from the given URL and saves it as a file."""
  response = requests.get(url, stream=True)
  if response.status_code == 200:
    with open(filename, 'wb') as out_file:
      for chunk in response.iter_content(1024):
        if chunk:
          out_file.write(chunk)
  else:
    print(f"Error downloading image: {response.status_code}")

# Example usage:
image_url = "https://example.com/image.jpg"  # Replace with the actual image URL
filename = "card_image.jpg"
download_image(image_url, filename)
