from flask import Flask, render_template, redirect, url_for
from flask_mail import Mail,  Message

app = Flask(__name__)
app.config.update(
    MAIL_SERVER='prueba@gmail.com',
    MAIL_PORT=587,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'thaliaaguilar2909@gmail.com',
    MAIL_PASSWORD = 'Thalia97'
)

mail = Mail(app)

@app.route('/send-mail/')
def send_mail():
    msg = mail.send_message(
        'Send Mail tutorial!',
        sender='thaliaaguilar2909@gmail.com',
        recipients=['darvictor5@msn.com'],
        body="Congratulations you've succeeded!"
    )
    return 'Mail sent'
