import requests
from bs4 import BeautifulSoup

def scrape_page(url, arr):
    response = requests.get(url, headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.content, "html.parser")
    sections = soup.find_all("section", class_="jobs")[0:]
    for section in sections:
        jobs = section.find_all("li")[0:]
        for job in jobs:
            if(job.find("span", class_="company") != None):
                company = job.find("span", class_="company").text
                title = job.find("span", class_="title").text
                url = job.find("a")["href"]
                job_data = {
                    'title': title,
                    'company': company,
                    'url': url
                }
                arr.append(job_data)