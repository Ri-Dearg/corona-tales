import os
from flask import Flask, render_template, url_for, request, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'corona_tales'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

stories = mongo.db.stories

taglist = set()

for story in stories.find():
    tags = story["tags"]
    for tag in tags:
        taglist.add(tag)


@app.route('/')
def story_page():
    storylist = stories.find()
    return render_template('index.html', storylist=storylist, taglist=taglist)


@app.route('/create_story', methods=['POST'])
def create_story():
    stories.insert_one(request.form.to_dict())
    return redirect(url_for('story_page'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
