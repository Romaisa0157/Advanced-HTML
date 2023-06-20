from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Email content
    subject = 'New Contact Form Submission'
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    email_message = f"Subject: {subject}\n\n{body}"

    # Configure your email settings
    sender_email = 'romaisa0157@gmail.com'  # your email address
    sender_password = '15july_2004'  # your email password
    recipient_email = 'romaisa0157@gamil.com'  # recipient email address

    try:
        # Connect to the email server
        server = smtplib.SMTP('smtp.gmail.com', 587)  # assuming you're using Gmail
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, email_message)
        server.quit()

        return 'Thank you for your submission! We will be in touch.'
    except Exception as e:
        return f'An error occurred while sending the email: {str(e)}'
        
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
