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
            language = book['language']

            print(f"Title: {title}")
            print(f"Author(s): {author}")
            print(f"Languages: {language}")
            # blank line between books
            print()   
            
            # i need this in the loop so it gets all the books not just one
            all_books.append({
                "Genre": genre,
                "Title": title,
                "Author(s)": author,
                "Languages": language
            })

    else:
        print(f"Unable to get data for genre: {genre}")
        print()
# csv file

df = pd.DataFrame(all_books)
df.to_csv("Books_By_Genre.csv", index=False)

# Generative AI with Ollama
API_URL = "http://127.0.0.1:11434/api/generate"  # Ollama local API

def generate_text(prompt, model="tinyllama", stream=False):
    """
    Generate text using Ollama API
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": stream
    }
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            return result.get("response", "")
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

# Generate AI discussions for each book
ai_discussions = []

for book in all_books:
    title = book["Title"]
    prompt = f"Generate 3-5 discussion questions for a virtual book club reading '{title}'."

    discussion = generate_text(prompt)
    print(f" AI Discussion for '{title}':\n{discussion}\n")

    ai_discussions.append({
        "Title": title,
        "AI_Discussion": discussion
    })
#Gradio App
import requests
API_URL = "http://127.0.0.1:11434/api/generate"  # Ollama local API

def generate_text(prompt, model="tinyllama", stream=False):
    payload = {"model": model, "prompt": prompt, "stream": stream}
    try:
        resp = requests.post(API_URL, json=payload, timeout=60)
        if resp.status_code == 200:
            data = resp.json()
            return data.get("response", "")
        return f"Error {resp.status_code}: {resp.text}"
    except Exception as e:
        return f"Error: {e}"
def team_chat(message, history):
  
    header = (
        "You are a concise Book Club assistant. "
        "Use short, helpful replies. If asked, you can craft 3–5 discussion questions for a book.\n\n"
        "Conversation so far:\n"
    )
    convo = []
    for u, a in history:
        if u: convo.append(f"User: {u}")
        if a: convo.append(f"Assistant: {a}")
    convo.append(f"User: {message}")
    convo.append("Assistant:")

    prompt = header + "\n".join(convo)
    return generate_text(prompt) 
with gr.Blocks() as demo:
    gr.ChatInterface(
        fn=team_chat,
        title="Book Club Chat (Team API)",
        description="Chat is powered by our team's AI. Ask about books or request 3–5 discussion questions for a title.",
        examples=[
            "Give 3–5 discussion questions for 'The Hobbit'.",
            "Summarize why people enjoy mystery novels.",
            "Recommend a fantasy book for beginners and why."
        ]
    )

# Launch the app with a public link
if __name__ == "__main__":
    demo.launch(share=True)
