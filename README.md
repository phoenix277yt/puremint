# PureMint: Personalized Toothpaste Recommendation

**PureMint** is an AI-powered web application that provides personalized toothpaste recommendations based on your dental health profile. By analyzing user inputs about cavity risk, sensitivity, gum health, and other factors, PureMint generates a list of science-backed ingredients tailored to your wellness needs.

---

## 🚀 Features

- **AI-Based Ingredient Selection**: Uses user inputs to recommend toothpaste ingredients tailored to dental needs.
- **In-Depth Form**: Collects detailed information such as cavity risk, sensitivity level, plaque buildup, and more.
- **Focus on Sustainability**: Includes natural and organic ingredient preferences for environmentally-conscious users.
- **Custom Recommendations**: Ingredients are carefully selected based on dental science and user preferences.

---

## 🖥️ Live Demo

Coming soon!

---

## 📸 Screenshots

### Home Page
A simple and intuitive form where users can input their dental profile.

> _Add screenshots here once the UI is complete._

---

## 🛠️ Technology Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML5, CSS (optional for styling)
- **AI Logic**: Python-based recommendation algorithm
- **Deployment**: Flask development server (can be hosted on platforms like Heroku or AWS)

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
git clone https://github.com/yourusername/PureMint.git
cd PureMint
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
- Plaque Control: Rarely, Occasionally, Often
- Breath Freshening Importance: Not Important, Somewhat Important, Very Important
- Special Conditions: None, Braces, Implants, Other
- Tartar Control: Yes, No
- Organic Preference: Yes, No Preference
- Flavor Preference: Mint, Citrus, Herbal, No Preference

---

## 💡 How It Works
1. User submits the form with their dental health details.
2. The backend processes the inputs and uses an algorithm to determine the best toothpaste ingredients.
3. A list of recommended ingredients is displayed on the same page.

---

## 🧠 Future Enhancements
- Add more advanced AI models for ingredient selection.
- Build a database to store user profiles and ingredient information.
- Improve UI/UX with CSS and JavaScript interactivity.
- Host the project online for public access.

---

## 💖 Contributing
### Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch ``git checkout -b feature-name``.
3. Commit changes ``git commit -m "Description"``.
4. Push to the branch ``git push origin feature-name``.
5. Open a pull request.

---

### 📜 License
This project is licensed under the Apache v2 License.

### ✨ Acknowledgments
Thanks to Flask for making backend development simple.
Inspiration from the focus on sustainability and wellness.
An entry for the Technasia 5.0 hackathon.
