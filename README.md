# Web Scraper App – Flask + Docker

Welcome to the **Advanced Web Scraper**, a lightweight yet flexible web application built using **Flask** and **BeautifulSoup**. This app allows you to extract structured content from any public webpage — whether you're gathering headlines, collecting links, or targeting specific elements with custom tags or classes.

With just a URL and a click, you can scrape the data you need and **export it directly to a CSV file**. Everything runs inside a clean, responsive web UI — no coding or browser extensions needed.



## Key Features

**User-friendly Web Interface** – Built with Flask and Bootstrap
**Scrape What You Need** – Choose from:
   All `<h1>`, `<h2>`, and `<h3>` headings
   All clickable `<a href>` links
   Custom HTML tags (like `div`, `p`, `span`, etc.)
   Elements by class name (`class="your-class"`)
   **Download to CSV** – Save results with one click
   **Docker-Ready** – Easily containerize and deploy anywhere


## Technologies Used

- **Python 3.11**
- **Flask** – lightweight web framework
- **BeautifulSoup** – for HTML parsing
- **Bootstrap 5** – responsive front-end
- **Docker** – for containerized deployment



You can run this app locally with Python or spin it up in seconds using Docker.

###  Option 1: Local Python Setup

####  Requirements
- Python 3.8 or newer
- pip (Python package manager)
  
- # Clone the repository
git clone https://github.com/your-username/web_scraper_flask.git
cd web_scraper_flask

# create a virtual envirment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# install python dependencies
pip install -r requirements.txt

# run the Flask app
python app.py

# run without docker
pip install -r requirements.txt
python app.py

#run with docker
docker build -t flask-web-scraper .
docker run -p 5000:5000 flask-web-scraper


