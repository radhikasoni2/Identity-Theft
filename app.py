'''from flask import Flask, render_template, request

app = Flask(__name__)

# List of known phishing domains (replace with an updated list)
phishing_domains = {
    "example1.com",
    "example2.net",
    "example3.org"
}

@app.route("/")
def index():
    return render_template("index.html", result="")

@app.route("/check", methods=["GET", "POST"])  # Allow both GET and POST requests
def check_phishing():
    if request.method == "POST":
        user_input = request.form["url"]
        domain = user_input.split("//")[-1].split("/")[0]

        if domain in phishing_domains:
            result = "This website is a known phishing website!"
        else:
            result = "This website appears to be safe."

        return render_template("index.html", result=result)
    else:
        # Handle GET requests (e.g., when accessing /check directly in the browser)
        return render_template("index.html", result="")

if __name__ == "__main__":
    app.run(debug=True)'''

'''2
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# PhishTank API endpoint
PHISHTANK_API_URL = "http://checkurl.phishtank.com/checkurl/"

# Your PhishTank API key (sign up for one on the PhishTank website)
PHISHTANK_API_KEY = "YOUR_API_KEY"

@app.route("/")
def index():
    return render_template("index.html", result="")

@app.route("/check", methods=["POST"])
def check_phishing():
    if request.method == "POST":
        user_input = request.form["url"]

        # Send a POST request to the PhishTank API for URL verification
        response = requests.post(PHISHTANK_API_URL, data={"url": user_input, "format": "json", "app_key": PHISHTANK_API_KEY})

        if response.status_code == 200:
            data = response.json()
            if data["results"]["in_database"]:
                result = "This website is a known phishing website!"
            else:
                result = "This website appears to be safe."
        else:
            result = "Error checking the URL."

        return render_template("index.html", result=result)
    else:
        return render_template("index.html", result="")

if __name__ == "__main__":
    app.run(debug=True) '''

from flask import Flask, render_template, request

app = Flask(__name__)

def is_phishing(url):
    # Define a list of known phishing websites
    phishing_websites = [
        "f34233.com",
        "f29481.com",
        # Add more phishing websites as needed
    ]

    for phishing_site in phishing_websites:
        if phishing_site in url:
            return True

    return False

@app.route("/")
def index():
    return render_template("index.html", result="")

@app.route("/check", methods=["POST"])
def check_phishing():
    if request.method == "POST":
        user_input = request.form["url"]

        if is_phishing(user_input):
            result = "This website is a known phishing website!"
        else:
            result = "This website appears to be safe."

        return render_template("index.html", result=result)
    else:
        return render_template("index.html", result="")

if __name__ == "__main__":
    app.run(debug=True)
