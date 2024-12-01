import psutil
import smtplib
from email.mime.text import MIMEText
import time

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Typically 587 for TLS
USERNAME = 'srinu9948813039@gmail.com'  # Your email address
PASSWORD = 'Sai@Naveen143'  # Your email password
TO_EMAIL = 'srinu9948813039@gmail.com'  # Recipient's email address

def send_alert(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = USERNAME
    msg['To'] = TO_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(USERNAME, PASSWORD)
            server.sendmail(USERNAME, TO_EMAIL, msg.as_string())
        print("Alert sent successfully!")
    except Exception as e:
        print(f"Failed to send alert: {e}")

def monitor_cpu_usage(threshold=1):
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)  # Get CPU usage over 1 second
        print(f"Current CPU Usage: {cpu_usage}%")
        
        if cpu_usage > threshold:
            send_alert('CPU Usage Alert', f'CPU usage is at {cpu_usage}%')
        
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    monitor_cpu_usage()
