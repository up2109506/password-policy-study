from flask import Flask, render_template, request, jsonify
import csv
import time

app = Flask(__name__)

@app.route("/")
def consent():
    return render_template("consent.html")

@app.route("/test")
def index():
    return render_template("index.html")

from flask import send_file

@app.route("/download")
def download():
    return send_file("data.csv", as_attachment=True)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json

    session_id = data["session_id"]
    policy_id = data["policy_id"]
    policy_type = data["policy_type"]
    time_taken = data["time"]
    attempts = data["attempts"]
    length = data["length"]
    strength = data["strength"]

    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([session_id, policy_id, policy_type, time_taken, attempts, length, strength])

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
