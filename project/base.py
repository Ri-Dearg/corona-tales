from flask import Blueprint, current_app, render_template, url_for, request, redirect
from bson.objectid import ObjectId

base = Blueprint('base', __name__,
                   template_folder='templates')

taglist = set()


@base.route('/')
def story_page():

    stories = current_app.config['stories']

    for story in stories.find():
        tags = story["tags"]
        for tag in tags:
            taglist.add(tag)

    storylist = stories.find()
    return render_template('index.html', storylist=storylist, taglist=taglist)


@base.route('/signup')
def signup():

    return render_template('signup.html')


@base.route('/create_story', methods=['POST'])
def create_story():
    stories = current_app.config['stories']

    stories.insert_one(request.form.to_dict(flat=False))
    return redirect(url_for('story_page'))
