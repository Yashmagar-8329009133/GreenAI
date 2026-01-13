from flask import Flask, render_template, request, jsonify, session
from model import predict_sustainability

app = Flask(__name__)
app.secret_key = "greenai_secret_key"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/predict', methods=["POST"])
def predict():
    data = request.get_json()
    score = predict_sustainability(data)

    session['last_analysis'] = {
        "score": score,
        "energy": data.get("energy"),
        "water": data.get("water"),
        "co2": data.get("co2"),
        "renewable": data.get("renewable"),
        "waste": data.get("waste")
    }

    return jsonify({"score": score})

@app.route('/report')
def report():
    analysis = session.get('last_analysis')
    return render_template("report.html", analysis=analysis)

if __name__ == "__main__":
    app.run(debug=True)
