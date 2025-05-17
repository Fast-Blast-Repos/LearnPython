# This file contains functions to get data from various free APIs for YOUR projects.

import requests
from bs4 import BeautifulSoup

def bible_verse():
    try:
        # Use the Bible API to get a random Bible verse
        response = requests.get("https://bible-api.com/data/kjv/random")
        if response.status_code == 200:
            data = response.json()
            verse_text = data.get('random_verse', {}).get('text', 'Verse not found')
            return verse_text
        else:
            print(f"Failed to fetch data. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def dev_excuse():
    try:
        # Use the Developer Excuses API to get a random excuse
        response = requests.get("http://developerexcuses.com/")
        if response.status_code == 200:
            # Parse the HTML response
            soup = BeautifulSoup(response.text, 'html.parser')
            excuse = soup.find('a').text.strip()  # Extract the text inside the <a> tag
            return excuse
        else:
            print(f"Failed to fetch data. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def advice():
    try:
        # Use the Advice Slip API to get a random piece of advice
        response = requests.get("https://api.adviceslip.com/advice")
        if response.status_code == 200:
            data = response.json()
            advice_text = data.get('slip', {}).get('advice', 'Advice not found')
            return advice_text
        else:
            print(f"Failed to fetch data. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def dev_joke():
    try:
        # Use the Joke API to get a random dev joke
        response = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single")
        if response.status_code == 200:
            data = response.json()
            joke_text = data['joke']
            return joke_text
        else:
            print(f"Failed to fetch data. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def cat_fact():
    # Use the Cat Facts API to get a random cat fact
    try:
        response = requests.get("https://catfact.ninja/fact")
        if response.status_code == 200:
            data = response.json()
            fact = data["fact"]
            return fact
        else:
            print(f"Failed to fetch data. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


print("Random Bible Verse:")
print(bible_verse())
print("\nDeveloper Excuse:")
print(dev_excuse())
print("\nRandom Advice:")
print(advice())
print("\nRandom Dev Joke:")
print(dev_joke())
print("\nRandom Cat Fact:")
print(cat_fact())
# More APIs will be added here