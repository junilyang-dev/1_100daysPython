from flask import Flask, render_template, request
import berlinstartupjobs
import weworkremotely
import web3

app = Flask("JobScrapper")
siteaddress = ["https://berlinstartupjobs.com/skill-areas/","https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term=","https://web3.career/"]
site = ["berlinstartupjobs","weworkremotely","web3"]

@app.route('/')
def search():
    return render_template('search.html')

@app.route('/result', methods=['POST'])
def result():
    website = request.form['website']
    websiteNm = site[int(website)-1]
    skill = request.form['skill']
    scraped_data = web_scraper(website, skill)
    return render_template('result.html', website=websiteNm, skill=skill, data=scraped_data)

def web_scraper(website, skill):
    url = siteaddress[int(website)-1] + skill
    data = []
    if website == '1':
      berlinstartupjobs.scrape_page(url, data)
    elif website == '2':
      weworkremotely.scrape_page(url, data)
    else:
      web3.get_pages(url, data)
    return data
app.run("0.0.0.0")