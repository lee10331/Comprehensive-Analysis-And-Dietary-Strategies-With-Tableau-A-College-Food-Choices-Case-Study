📊 Project Overview
This project aims to support healthy food choices among college students by visualizing survey data through a dashboard and a data-driven story. We used Tableau for creating the visuals and Flask to embed them into a simple, user-friendly web app.

🔧 Tools & Technologies Used
Tableau Public – For creating dashboards and stories

Python – As the programming language

Flask – A lightweight Python web framework to serve the visuals

HTML/CSS – For structuring and styling the frontend

VS Code / PyCharm – For code editing

Browser – To preview the local web app

📌 Step-by-Step Implementation
1. Data Cleaning and Visualization (Tableau)
Cleaned the dataset in Python using pandas, based on a given codebook.

Exported the cleaned data as .csv and imported it into Tableau.

Created a dashboard with filters like Gender and Grade Level and visuals covering food preferences, health perception, exercise, and eating habits.

Built a story in Tableau using multiple dashboards to narrate insights and help guide healthier choices.

Published both the dashboard and story to Tableau Public and copied the embed code.

2. Flask Web App Setup
Created a new folder with:
app.py
templates/
    ├── dashboard.html
    └── story.html
   
Wrote a basic Flask app in app.py:

3. Embedding Tableau Dashboard and Story
Inside dashboard.html and story.html, we:

Pasted the Tableau embed code

Adjusted styling and responsiveness

Used <div class='tableauPlaceholder'>...</div> and loaded viz_v1.js for full functionality

4. Running the App Locally
Launched the Flask app:


Opened the app in the browser:

http://127.0.0.1:5000/ → Dashboard

http://127.0.0.1:5000/story → Story

📁 Final Folder Structure

├── app.py
├── templates/
│   ├── dashboard.html
│   └── story.html
✅ Outcome
The dashboard provides insights on food behavior and preferences.

The story walks viewers through key data points in an engaging narrative format.

The Flask integration presents both views in a clean, simple local web app.
