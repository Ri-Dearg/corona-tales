import os
from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'corona_tales'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
def story_page():
    return render_template('index.html', stories=mongo.db.stories.find())


@app.route('/create_story', methods=['POST'])
def create_story():
    stories = mongo.db.stories
    stories.insert_one(request.form.to_dict())
    return redirect(url_for('story_page'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
