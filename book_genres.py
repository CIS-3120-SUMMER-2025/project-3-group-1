# import libaries
import requests
import pandas as pd
import json
from urllib.parse import quote
import time

# Set the genres
genres=['romance', 'foreign language learning', 'mystery', 'fantasy']

# Limit per genre
limit = 30

all_books = []
i = 0
for genre in genres:
    encoded_genre = quote(genre)
    url = f"https://openlibrary.org/search.json?subject={encoded_genre}&limit={limit}"

    if i % 2 == 0:
        print("Sleeping zzzzzz")
        time.sleep(3)
    i += 1

    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()

        print(f"📚 Genre: {genre}")

        for book in data['docs']:
            title = book['title']
            author = book['author_name']
            year = book['first_publish_year']
            language = book['language']

            print(f"Title: {title}")
            print(f"Author(s): {author}")
            print(f"First Published: {year}")
            print(f"Languages: {language}")
            # blank line between books
            print()   
            
            # i need this in the loop so it gets all the books not just one
            all_books.append({
                "Genre": genre,
                "Title": title,
                "Author(s)": author,
                "First Published": year,
                "Languages": language
            })

    else:
        print(f"Unable to get data for genre: {genre}")
        print()
# csv file

df = pd.DataFrame(all_books)
df.to_csv("Books_By_Genre.csv", index=False)
