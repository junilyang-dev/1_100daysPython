import requests
from bs4 import BeautifulSoup

all_jobs = []


def scrape_page(url, arr):
    print(url)
    response = requests.get(url, headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"})
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
        arr.append(job_data)


def get_pages(url):
    response = requests.get(url, headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.content, "html.parser",)
    return len(soup.find("ul", class_="bsj-nav").find_all("a"))


# total_pages = get_pages("https://berlinstartupjobs.com/engineering")

# for x in range(total_pages-1):
#     url = f"https://berlinstartupjobs.com/engineering/page/{x+1}"
#     scrape_page(url, all_jobs)


# print(len(all_jobs))

all_skill_href = []


def get_skill(url):
    response = requests.get(url, headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.content, "html.parser",)
    links_box = soup.find("div", class_="popular_skills").find(
        "ul", class_="links-box").find_all("li", class_="link")[0:]
    for links in links_box:
        link = links.find("a")["href"]
        all_skill_href.append(link)


# get_skill("https://berlinstartupjobs.com/engineering")


all_jobs_skill = []


def scrape_page_skill(url):
    response = requests.get(url, headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.content, "html.parser",)
    jobs = soup.find("ul", class_="jobs-list-items").find_all("li")[0:]


# for skill_href in all_skill_href:
#     scrape_page(skill_href, all_jobs_skill)
# print("all_jobs_skill")
# print(len(all_jobs_skill))
