from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/sustainability")
def sustainability():
    return render_template("sustainability.html")

@app.route('/recommend', methods=['POST'])
def recommend():
    # Collecting form data
    age = request.form['age']
    cavity_risk = request.form['cavity_risk']
    sensitivity = request.form['sensitivity']
    gum_health = request.form['gum_health']
    whitening = request.form['whitening']

    # Simpler recommendation logic with a smaller list of ingredients
    ingredients = []

    # Special
    if special == "kid":
        ingredients.append("Bubblegum Flavour")
    elif special == "old":
        ingredients.extend(["Proprietary Gentledent Formula"], ["Chamomile"])
    elif special == "veg":
        ingredients.append("Organic Alternatives")
    elif special == "sport":
        ingredients.extend(["Remineralization Salt"], ["Rehydration Salt"], ["Probiotics"], ["Mint"]) 

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
        ingredients.extend(["Aloe Vera", "Coenzyme Q10"])
    elif gum_health == "Moderate":
        ingredients.append("Eucalyptus Extract")
    
    # Whitening
    if whitening == "Yes":
        ingredients.extend(["Activated Charcoal", "Baking Soda"])

    # Plaque Reduction and Freshening
    ingredients.extend(["Triclosan", "Menthol and Peppermint Oil"])

    return render_template('index.html', ingredients=ingredients)


if __name__ == "__main__":
    app.run(debug=True)
