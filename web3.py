import requests
from bs4 import BeautifulSoup
import re

def scrape_page(url, arr):
    response = requests.get(url, headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("tbody", class_="tbody").find_all("tr", attrs={"data-jobid": True})[0:]
    for job in jobs:
        company = job.find("h3").text
        title = job.find("div", class_="mb-auto").find("h2", class_="fs-6 fs-md-5 fw-bold my-primary").text
        job_data = {
            'title': title,
            'company': company
        }
        arr.append(job_data)


def get_pages(url, arr):
    url = url + "-jobs"
    response = requests.get(url, headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.content, "html.parser",)
    pTot = soup.find("p", id="hh").text
    tot = int(re.search(r'\d+', pTot).group())
    pages = int(tot / 25)
    print(pages)
    for i in range(1, pages+1):
        nUrl = url + f"?page={i}"
        scrape_page(nUrl, arr)
