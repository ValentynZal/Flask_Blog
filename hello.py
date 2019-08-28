from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Valera',
        'title': 'Some',
        'content': 'Bal bla  bla',
        'date': 'August 28, 2019'
    },
    {
        'author': 'Vita',
        'title': 'Some',
        'content': 'Bal bla  bla',
        'date': 'August 27, 2019'
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

if __name__ == '__main__':
    app.run(debug=True)