from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import CONFIG

def send_email_alerts(jobs):
    if not jobs:
        return
        
    message = Mail(
        from_email=CONFIG['email']['sender'],
        to_emails=CONFIG['email']['recipient'],
        subject="Your Daily Job Alerts"
    )
    
    html_content = "<h2>New Job Alerts</h2><ul>"
    for job in jobs:
        html_content += f"""
        <li>
            <strong>{job['title']}</strong> at {job['company']}<br>
            <a href="{job['link']}">Apply Here</a>
        </li>
        """
    html_content += "</ul>"
    
    message.content = Mail("text/html", html_content)
    
    try:
        sg = SendGridAPIClient(CONFIG['email']['sendgrid_api_key'])
        response = sg.send(message)
        print(f"Email sent! Status: {response.status_code}")
    except Exception as e:
        print(f"Email failed: {e}")
