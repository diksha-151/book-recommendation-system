# 📚 Book Recommendation System: Webhook using Flask + IBM Watsonx Assistant

This project is a **Flask-based webhook** designed to integrate with **IBM Watsonx Assistant**. It helps build a conversational **book recommendation system** that suggests books based on user preferences like **genre** or **mood**.

---

## Try the Chatbot Live

[Click here to chat with the Book Recommender Chatbot]
https://web-chat.global.assistant.watson.appdomain.cloud/preview.html?backgroundImageURL=https%3A%2F%2Feu-de.assistant.watson.cloud.ibm.com%2Fpublic%2Fimages%2Fupx-a63d18c8-ac11-4a44-8b5e-c1f4e65a40ba%3A%3Afe8a8ee0-9b38-4c08-bdb3-85d6e06593fd&integrationID=cc7c6387-ffdf-42c9-8d21-a8211c0abe0e&region=eu-de&serviceInstanceID=a63d18c8-ac11-4a44-8b5e-c1f4e65a40ba


## 🚀 How It Works

1. The user chats with the Watsonx Assistant chatbot and mentions a genre or mood.
2. Watsonx sends that input to this Flask webhook using a **POST request**.
3. The webhook reads a local `books.csv` file containing a book dataset.
4. It filters matching books by genre or mood and returns a list of recommendations as a JSON response.

---

## 🗂️ Project Structure

book-recommender/
├── main.py # Flask webhook code
├── books.csv # Dataset of books
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## 🧠 Sample Dataset (`books.csv`)

⚙️ How to Run the Webhook Locally
✅ Prerequisites
Python installed (3.x)

Flask installed

🛠 Installation Steps
Clone the repository or download the ZIP

Navigate to the project folder

Install Flask
Run the Flask server
python main.py
The server will start on http://localhost:5000/recommend

🤖 Integration with IBM Watsonx Assistant
In Watsonx, create a Dialog Skill and set up:

Intent: #recommend_books

Entity: @genre, @mood (example: Fantasy, Thriller, Romantic, etc.)

Add a dialog node that:

Captures user input (genre or mood)

Calls this webhook URL using POST

Display the response in the chatbot output using <?webhook_result?>

📦 requirements.txt

flask

pandas

Created by [Diksha Patel]

For educational purposes — Book Recommender using Watsonx + Python
