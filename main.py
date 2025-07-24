from job_scraper import scrape_jobs
from job_filter import filter_jobs
from email_sender import send_email_alerts
import json
import os
from datetime import datetime

def load_sent_jobs():
    if not os.path.exists('sent_jobs.json'):
        return []
    with open('sent_jobs.json', 'r') as f:
        return json.load(f)

def save_sent_jobs(jobs):
    with open('sent_jobs.json', 'w') as f:
        json.dump(jobs, f)

def main():
    print(f"Running job alerts at {datetime.now()}")
    all_jobs = scrape_jobs()
    filtered_jobs = filter_jobs(all_jobs)
    sent_jobs = load_sent_jobs()
    
    new_jobs = [job for job in filtered_jobs if job['link'] not in sent_jobs]
    
    if new_jobs:
        send_email_alerts(new_jobs)
        sent_jobs.extend([job['link'] for job in new_jobs])
        save_sent_jobs(sent_jobs)
        print(f"Sent {len(new_jobs)} alerts")
    else:
        print("No new jobs")

if __name__ == "__main__":
    main()
