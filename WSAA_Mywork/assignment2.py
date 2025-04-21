# Import dependencies

import requests
import json

# Create and shuffle a new deck of card
deck_shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(deck_shuffle_url)
deck_response = response.json()
print (deck_response)

# get the deck id from the response 
deck_id = deck_response["deck_id"]
print (deck_id)

# Draw 5 cards with from the deck with the deck id
draw_card_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(draw_card_url)
draw_response = response.json()["cards"]

# Save the drawn card response to a file a
with open ("deckresponse.json", "w") as dr:
    json.dump(draw_response, dr, indent=4)

# printing the drawn cards by looping through the response
for card in draw_response:
    print(f"{card['value']} is {card['suit']}")