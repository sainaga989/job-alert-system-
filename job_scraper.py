import requests
from bs4 import BeautifulSoup
from config import CONFIG

def scrape_naukri():
    try:
        url = "https://www.naukri.com/data-analyst-jobs-in-bangalore"
        headers = {'User-Agent': CONFIG['scraping']['user_agent']}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        jobs = []
        for job in soup.find_all('article', class_='jobTuple'):
            title = job.find('a', class_='title').text.strip()
            company = job.find('a', class_='subTitle').text.strip()
            link = job.find('a', class_='title')['href']
            jobs.append({
                'title': title,
                'company': company,
                'link': link,
                'source': 'Naukri'
            })
        return jobs
    except Exception as e:
        print(f"Naukri scraping failed: {e}")
        return []

def scrape_jobs():
    return scrape_naukri()  # Add other scrapers here later
