from flask import (Blueprint, current_app, render_template, url_for, request,
                   redirect)
from flask_login import login_required, current_user
from .extensions import mongo

base = Blueprint('base', __name__,
                 template_folder='templates')

stories = mongo.db.stories
story_list = stories.find()

@base.route('/')
def story_page():
    
    taglist = current_app.config['taglist']

    for story in stories.find():
        tags = story["tags"]
        for tag in tags:
            taglist.add(tag)

    return render_template('index.html', story_list=story_list, taglist=taglist,
                           username=current_user.username)


@base.route('/create_story', methods=['POST'])
def create_story():

    stories.insert_one(request.form.to_dict(flat=False))
    return redirect(url_for('base.story_page'))


@base.route('/profile')
@login_required
def profile():

    user_stories = stories.find({'username': current_user.username})

    return render_template("profile.html", username=current_user.username,
                           userstories=user_stories)
