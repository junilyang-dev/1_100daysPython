import requests 
from bs4 import BeautifulSoup

all_jobs = []

def scrape_page(url):
  response = requests.get(url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"})
  soup = BeautifulSoup(response.content, "html.parser",)
  jobs = soup.find("ul", class_="jobs-list-items").find_all("li")[0:]

  for job in jobs:
    company = job.find("a", class_="bjs-jlid__b").text
    title = job.find("h4", class_="bjs-jlid__h").text
    desc = job.find("div", class_="bjs-jlid__description").text 
    url = job.find("h4", class_="bjs-jlid__h").find("a")["href"]

    job_data = {
      'title': title,
      'company': company,
      'desc': desc,
      'url': url
    }
    all_jobs.append(job_data)

def get_pages(url):
  response = requests.get(url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"})
  soup = BeautifulSoup(response.content, "html.parser",)
  return len(soup.find("ul", class_="bsj-nav").find_all("a"))

total_pages = get_pages("https://berlinstartupjobs.com/engineering")

for x in range(total_pages-1):
  url = f"https://berlinstartupjobs.com/engineering/page/{x+1}"
  scrape_page(url)


print(len(all_jobs))