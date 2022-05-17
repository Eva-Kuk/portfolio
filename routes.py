import os
from flask import Flask, render_template, request
from forms import ContactForm

if os.path.exists("env.py"):
    import env

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        return 'Form posted.'

    elif request.method == 'GET':

        return render_template('contact.html', form=form)


# Set how & where to run the app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
