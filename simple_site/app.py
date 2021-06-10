import os

from flask import Flask, render_template, request

template_dir = os.path.abspath('../templates')
app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        'index.html',
        title="We make you miss your flat flat",
    )

@app.route("/signin", methods=['POST'])
def signin():
    if not request.form.get('testament'):
        testament_message = 'You better have testament. We warned you'
    else:
        testament_message = ""

    return render_template(
        'sign_result.html',
        name=request.form['name'],
        title="You are signed in",
        warning=testament_message,
    )


if __name__ == '__main__':
    app.run("0.0.0.0", 5003)
