from flask import Flask,render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Anurag Singh',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 04, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'December 04, 2018'
    }
]

@app.route('/')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About Us')

if __name__ == '__main__':
    app.run(debug=True)
