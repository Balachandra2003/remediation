import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

run_id = sys.argv[1]
repo   = sys.argv[2]
dispatch_token = sys.argv[3]

SMTP_HOST = "YOUR_SMTP_HOST"
SMTP_PORT = 587
SMTP_USER = "YOUR_SMTP_USER"
SMTP_PASS = "YOUR_SMTP_PASS"
TO_EMAIL  = "YOUR_TO_EMAIL"

WEBHOOK = "https://your-webhook-domain.com"  # B1 secure webhook

# B1 secure links
approve_b1 = f"{WEBHOOK}/approve?run_id={run_id}"
skip_b1    = f"{WEBHOOK}/skip?run_id={run_id}"

# B2 insecure fallback
approve_b2 = f"https://api.github.com/repos/{repo}/actions/workflows/approval.yml/dispatches?token={dispatch_token}&run_id={run_id}"
skip_b2    = f"https://api.github.com/repos/{repo}/actions/workflows/skip.yml/dispatches?token={dispatch_token}&run_id={run_id}"

html = f"""
<h2>⚠️ Vulnerabilities Detected</h2>

<b>Secure Webhook Links (Recommended)</b><br>
<a href="{approve_b1}">Approve via Webhook</a><br>
<a href="{skip_b1}">Skip via Webhook</a><br><br>

<b>Unsafe Direct Trigger Links</b><br>
<a href="{approve_b2}">Approve (Insecure)</a><br>
<a href="{skip_b2}">Skip (Insecure)</a><br>
"""

msg = MIMEMultipart()
msg["From"] = SMTP_USER
msg["To"] = TO_EMAIL
msg["Subject"] = "Approval Required - Vulnerabilities Detected"
msg.attach(MIMEText(html, "html"))

server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
server.starttls()
server.login(SMTP_USER, SMTP_PASS)
server.sendmail(SMTP_USER, TO_EMAIL, msg.as_string())
server.quit()

print("Email sent successfully.")

