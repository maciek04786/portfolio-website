from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import smtplib
from email.message import EmailMessage
from flask_gravatar import Gravatar
import datetime

MY_EMAIL = "learningpython38@yahoo.com"
PASSWORD = 'bnzjqpcvbajximnf'

app = Flask(__name__)
app.config['SECRET_KEY'] = "430tuefwe8938wer9a823r49reszq"
Bootstrap(app)

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


def send_email(name, email, message):
    email_content = f"Name: {name}\n" \
                    f"Email: {email}\n" \
                    f"Message: {message}"

    msg = EmailMessage()
    msg['from'] = MY_EMAIL
    msg['to'] = email
    msg['subject'] = f"New blog message from {name}."
    msg.set_content(email_content)

    with smtplib.SMTP_SSL('smtp.mail.yahoo.com') as server:
        server.login(user=MY_EMAIL, password=PASSWORD)
        server.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=msg.as_string().encode('UTF-8'))



@app.route('/', methods=["GET", "POST"])
def home():
    current_year = datetime.date.today().year

    if request.method == "POST":
        data = request.form
        send_email(name=data["name"], email=data["email"], message=data["message"])

        return render_template("index.html", submit=True)

    return render_template("index.html", year=current_year, submit=False)



if __name__ == "__main__":
    app.run(debug=True)
