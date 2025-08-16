# project-3-group-1 - Virtual Book Club
AI-Enhanced Web App
<!-- purpose of the program --> In this project, we made an interactive Gradio-based web app where users can explore different book genres.  Chat with our book club AI, powered by our team's API. Getting book recommendations and 3-5 discussion questions for any title.

**The key points we did:**
Scrape real book data from Open Library by genre.
Generate discussion questions for each book using a generative AI model.
Provide an interactive chat interface via Gradio for virtual book club discussions.

**Github Repository** (https://github.com/CIS-3120-SUMMER-2025/project-3-group-1.git)
**Live App Link** (Ollama runs locally so a live app link is not available)
<!-- how to run the program --> 

#Step 1: 
-Clone the Repository 
git clone https://github.com/CIS-3120-SUMMER-2025/project-2-group-1.git 

#Step 2: 
-Install Dependencies 
pip install -r requirements.txt

Step 3:
Run the App Locally
python book_genres.py

Note: The AI functionality requires the Ollama model running locally at 127.0.0.1:11434. Without Ollama running, the app will not generate discussion questions.

<!-- each member's contributions -->
Loverta Brown: Opened the API by getting one and finding a book to filter each genre by webscraping. 
Nicole Ng: Used a generative AI model to create an output and input to collect the data, as well as correcting some information with the gradio app.
Paramjot Singh: Built an interactive front-end interface using Gradio/Streamlit where a user can input information and view results.
