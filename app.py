from flask import Flask, render_template, request

app = Flask(__name__)

# Enhanced recommendation function with science-backed ingredients
def recommend_ingredients(cavity_risk, sensitivity, gum_health, whitening):
    ingredients = []

    # Cavity Prevention
    if cavity_risk == "High":
        ingredients.extend(["Fluoride", "Nano-Hydroxyapatite", "Xylitol"])
    elif cavity_risk == "Medium":
        ingredients.extend(["Xylitol", "Green Tea Extract"])
    else:
        ingredients.append("Green Tea Extract")

    # Sensitivity Relief
    if sensitivity == "High":
        ingredients.extend(["Potassium Nitrate", "Calcium Carbonate"])
    elif sensitivity == "Medium":
        ingredients.append("Arginine and Calcium Carbonate")

    # Gum Health
    if gum_health == "Poor":
        ingredients.extend(["Aloe Vera", "Coenzyme Q10", "Tea Tree Oil"])
    elif gum_health == "Moderate":
        ingredients.extend(["Coenzyme Q10", "Eucalyptus Extract"])

    # Whitening
    if whitening == "Yes":
        ingredients.extend(["Activated Charcoal", "Baking Soda", "Hydrogen Peroxide"])

    # Plaque Reduction and Freshening
    ingredients.extend(["Triclosan", "Chlorhexidine", "Menthol and Peppermint Oil", "Zinc Citrate"])

    return ingredients

# Route to render form
@app.route('/')
def home():
    return render_template('index.html')

# Route to process form data
@app.route('/recommend', methods=['POST'])
def recommend():
    cavity_risk = request.form['cavity_risk']
    sensitivity = request.form['sensitivity']
    gum_health = request.form['gum_health']
    whitening = request.form['whitening']

    ingredients = recommend_ingredients(cavity_risk, sensitivity, gum_health, whitening)
    
    return render_template('index.html', ingredients=ingredients)

if __name__ == '__main__':
    app.run(debug=True)
