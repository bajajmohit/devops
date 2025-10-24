import requests
from bs4 import BeautifulSoup

url = "https://www.indeed.com/jobs?q=DevOps+Engineer&l=Dubai"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

for job in soup.select(".result"):
    title = job.select_one(".jobTitle span")
    company = job.select_one(".companyName")
    if title and company:
        print(f"{title.text} - {company.text}")
