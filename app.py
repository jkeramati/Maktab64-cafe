from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')



@app.route('/')
def hello_world():  # put application's code here
    return render_template("base_layout/_base.html")


if __name__ == '__main__':
    app.run(debug=True)
