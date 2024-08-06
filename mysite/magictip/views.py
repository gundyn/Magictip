import requests
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("Welcome to your MagicTip website!")  # Replace with your desired content

def get_card_image_url(card_name):
  """Fetches the image URL for a given card name from the Scryfall API."""
  url = f"https://api.scryfall.com/cards/named?fuzzy={card_name}"
  response = requests.get(url)
  if response.status_code == 200:
    card_data = response.json()
    return card_data['image_uris']['normal']
  else:
    return None

def card_image(request):
  card_name = "Mountain"  # Replace with your desired card name
  image_url = get_card_image_url(card_name)

  if image_url:
    context = {'image_url': image_url}
    return render(request, 'card_image.html', context)
  else:
    return HttpResponse("Error fetching image URL")  # For debugging
