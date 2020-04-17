from flask import (Blueprint, current_app, render_template, url_for, request,
                   redirect)
from bson.objectid import ObjectId

base = Blueprint('base', __name__,
                 template_folder='templates')


@base.route('/')
def story_page():

    stories = current_app.config['stories']
    taglist = current_app.config['taglist']

    for story in stories.find():
        tags = story["tags"]
        for tag in tags:
            taglist.add(tag)

    storylist = stories.find()
    return render_template('index.html', storylist=storylist, taglist=taglist)


@base.route('/create_story', methods=['POST'])
def create_story():

    stories = current_app.config['stories']

    stories.insert_one(request.form.to_dict(flat=False))
    return redirect(url_for('base.story_page'))

