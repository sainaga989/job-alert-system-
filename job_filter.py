from config import CONFIG

def filter_jobs(jobs):
    filtered = []
    for job in jobs:
        # Check keywords
        keyword_match = any(
            keyword.lower() in job['title'].lower() 
            for keyword in CONFIG['keywords']
        )
        
        # Check experience (simple version)
        exp_match = True  # Will implement proper check later
        
        if keyword_match and exp_match:
            filtered.append(job)
    return filtered
