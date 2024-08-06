import requests

def get_card_image_url(card_name):
  """Fetches the image URL for a given card name from the Scryfall API."""
  url = f"https://api.scryfall.com/cards/named?fuzzy={card_name}"
  response = requests.get(url)
  if response.status_code == 200:
    card_data = response.json()
    return card_data['image_uris']['normal']
  else:
    print(f"Error fetching card data: {response.status_code}")
    return None

# Example usage:
card_name = "Mountain"
image_url = get_card_image_url(card_name)
print(image_url)
