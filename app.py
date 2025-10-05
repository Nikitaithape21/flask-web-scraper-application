from flask import Flask, render_template, request, send_file
import requests
from bs4 import BeautifulSoup
import csv
import os

app = Flask(__name__)
last_results = []  # Global list to store scraped data

@app.route("/", methods=["GET", "POST"])
def index():
    global last_results
    results = None
    error = None

    if request.method == "POST":
        url = request.form.get("url")
        scrape_type = request.form.get("scrape_type")
        custom_value = request.form.get("custom_value")

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            if scrape_type == "headings":
                results = [h.get_text(strip=True) for h in soup.find_all(["h1", "h2", "h3"])]
            elif scrape_type == "links":
                results = [a['href'] for a in soup.find_all("a", href=True)]
            elif scrape_type == "tag" and custom_value:
                results = [tag.get_text(strip=True) for tag in soup.find_all(custom_value)]
            elif scrape_type == "class" and custom_value:
                results = [el.get_text(strip=True) for el in soup.find_all(class_=custom_value)]
            else:
                error = "Invalid option or missing custom input."

            last_results = results or []

        except Exception as e:
            error = f"An error occurred: {str(e)}"

    return render_template("index.html", results=last_results, error=error)

@app.route("/download")
def download_csv():
    global last_results

    if not last_results:
        return "No data to export.", 400

    filename = "scraped_data.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Scraped Content"])
        for item in last_results:
            writer.writerow([item])

    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
