from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_post, get_posts

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET': ## user views page with no interaction
        pass

    if request.method == 'POST': ## user has just entered some data values
        user_name = request.form.get('user_name')
        rating = request.form.get('rating')
        location = request.form.get('location')
        busy = request.form.get('busy')
        address = request.form.get('address')
        name = request.form.get('name')
        content = request.form.get('content')
        
        create_post(user_name, rating, location, busy, address, name, content)

    posts = get_posts()

    return render_template('postFeed.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
