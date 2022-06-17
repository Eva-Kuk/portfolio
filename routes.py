import os
from flask import (
    Flask, render_template, redirect, request, flash, url_for)
from flask_mail import Mail, Message
from forms import ContactForm
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# Configure server parameters

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'webdeveloperevakukla@gmail.com'
app.config["MAIL_PASSWORD"] = os.environ.get("MY_EMAIL_PASSWORD")
app.config["MAIL_USE_SSL"] = True
app.config['MAIL_USE_TLS'] = False


# Create an instance of the Mail class
mail = Mail(app)
# Set up secret key
app.secret_key = os.environ.get("SECRET_KEY")


# Home
@app.route('/')
def home():
    return render_template('home.html')


# About
@app.route('/about')
def about():
    return render_template('about.html')


# Projects
@app.route('/projects')
def projects():
    return render_template('projects.html')


# Contact
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        email = form.get("email")
        message = form.get("message")

        msg = Message(email,
            sender=("Ewa Kukla", email),
            recipients=['webdeveloperevakukla@gmail.com'])
        msg.body = message
        mail.send(msg)
        return redirect(url_for("contact"))

    return render_template("contact.html", form=form)

# Contact
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST' and form.validate():
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        msg = Message(
            subject=f"Mail from {name}",
            body=f"Name: {name}\nE-Mail: {email}\n\nSubject: {subject}n\n\n{message}",
            sender=email,
            recipients=['webdeveloperevakukla@gmail.com'])
        mail.send(msg)
        flash("Email Sent Successfully")
        return render_template("contact.html", success=True)

    return render_template("contact.html", form=form)


# Set how & where to run the app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
