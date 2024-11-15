# PureMint: Personalized Toothpaste Recommendation

**PureMint** is an AI-powered web application that provides personalized toothpaste recommendations based on your dental health profile. By analyzing user inputs about cavity risk, sensitivity, gum health, and other factors, PureMint generates a list of science-backed ingredients tailored to your wellness needs.

---

## 🚀 Features

- **AI-Based Ingredient Selection**: Uses user inputs to recommend toothpaste ingredients tailored to dental needs.
- **In-Depth Form**: Collects detailed information such as cavity risk, sensitivity level, plaque buildup, and more.
- **Focus on Sustainability**: Includes natural and organic ingredient preferences for environmentally-conscious users.
- **Custom Recommendations**: Ingredients are carefully selected based on dental science and user preferences.

---

## 🛠️ Technology Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML5, CSS
- **AI Logic**: Python-based recommendation algorithm
- **Deployment**: Flask development server

---

## 📂 Project Structure

``
PureMint/ 
  ├── app.py 
  ├── templates/ 
    │── index.html
    ├── static/
    ├── README.md
    └── requirements.txt
``

---

## 🛠️ Setup & Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/phoenix277yt/puremint.git
cd puremint
```
### 2. Install Dependencies
Ensure Python 3.x and pip are installed, then run:
```bash
pip install flask
```
### 3. Run the Application
Start the Flask server:
```bash
python app.py
```
Access the application in your browser at:
```bash
http://127.0.0.1:5000/
```

---

## 📋 User Input Form
#### The form collects the following data:

- Cavity Risk: Low, Medium, High
- Sensitivity Level: Low, Medium, High
- Gum Health: Good, Moderate, Poor
- Whitening Preference: Yes, No
- Organic Preference: Yes, No Preference
- Flavor Preference: Mint, Herbal, No Preference

---

## 💡 How It Works
1. User submits the form with their dental health details.
2. The backend processes the inputs and uses an algorithm to determine the best toothpaste ingredients.
3. A list of recommended ingredients is displayed on the same page.

---

### ✨ Acknowledgments
Thanks to Flask for making backend development simple.
Inspiration from the focus on sustainability and wellness.
An entry for the Technasia 5.0 hackathon.
