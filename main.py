import berlinstartupjobs

print("web scrapper")

print("1. berlinstartupjobs\n2. weworkremotely\n3. web3")
siteaddress = ["https://berlinstartupjobs.com","https://weworkremotely.com","https://web3.career"]
sitenum = int(input("enter number site : "))
print(sitenum, siteaddress[sitenum-1])

print("choose search lang\n1. python\n2. javascript\n3. java")
BprogramingLanguage = ["/skill-areas/python/", "/skill-areas/javascript/", "/skill-areas/java/"]
searchLang = int(input("enter number search lang: "))
print(searchLang, BprogramingLanguage[searchLang-1])
searchSite = siteaddress[sitenum-1] + BprogramingLanguage[searchLang-1]
print("search site : " + searchSite)

Barr = []
Warr = []
W3arr = []
all_jobs = [Barr, Warr, W3arr]
berlinstartupjobs.scrape_page(searchSite, all_jobs[sitenum-1])
print(all_jobs)