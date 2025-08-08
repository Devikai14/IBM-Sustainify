from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

def send_email(name, receiver_email):
    sender_email = "ibmsustainify@gmail.com"
    password = "edgd rizi fbeu brzm"

    subject = "Welcome to the Sustainability Project"
    body = f"""Hi {name},

Thank you for showing interest in our Proactive Community Sustainability Project.
We're excited to have you on board!

Regards,
The Sustainability Team"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.send_message(msg)
        print("✅ Email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", e)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    interests = request.form.getlist("interests")

    print(f"Received form: {name}, {email}, {interests}")

    send_email(name, email)

    flash("✔️ Thank you for joining! A confirmation email has been sent.")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
