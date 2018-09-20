"""This Module is used to create our web application main program by using Python3.6 or later"""
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '1cd6b93ae58c4162f65531e9015df0df'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

"xxxxx"    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User({self.username}, {self.email}, {self.image_file})'

"xxxxx"    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'Post({self.title}, {self.date_posted})'



posts= [
    {
        'author': 'Apichart Asavarojpanich',
        'title' : 'My first Flask Web',
        'content': 'My first content',
        'date_posted': 'Sep 1, 2018'
    },
    {
        'author': 'Test Asavarojpanich',
        'title' : 'My Second Flask Web',
        'content': 'My Second content',
        'date_posted': 'Sep 1, 2018'
    }
]

knowledgeinfo = [
    {
        'author': 'Apichart Asavarojpanich',
        'title': 'U18 - Image with Important Packages',
        'content': {
            '1' : 'vim',
            '2' : 'tmux',
            '3' : 'Python',
            '4' : 'PIP'
        },
        'date_posted': 'Sep 6, 2018'
    }        
        
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/knowledge")
def knowledge():
    return render_template('knowledge.html', knowledgeinfo=knowledgeinfo)
@app.route("/python")
def python():
    return render_template('python.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f' Account created for {form.username.data} ! ', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form) 

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form) 

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=5000)
