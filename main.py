from flask import Flask, request, jsonify
import pandas as pd

# Load dataset
books = pd.read_csv('books.csv')

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    genre = data.get('genre')
    mood = data.get('mood')

    filtered_books = books

    if genre:
        filtered_books = filtered_books[filtered_books['genre'].str.lower() == genre.lower()]
    if mood:
        filtered_books = filtered_books[filtered_books['mood'].str.lower() == mood.lower()]

    if not filtered_books.empty:
        book = filtered_books.sample(1).iloc[0]
        response_text = f"I recommend '{book['title']}' by {book['author']} ({book['genre']} - {book['mood']})"
    else:
        response_text = "Sorry, I couldn't find a suitable book."

    return jsonify({'output': {'generic': [{'response_type': 'text', 'text': response_text}]}})

if __name__ == '__main__':
    app.run(port=5000)