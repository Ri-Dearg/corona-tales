from flask import (Blueprint, current_app, render_template, url_for, request,
                   redirect)
from flask_login import login_required, current_user
from .extensions import mongo

base = Blueprint('base', __name__,
                 template_folder='templates')

stories = mongo.db.stories


@base.route('/')
def story_page():

    taglist = current_app.config['taglist']

    for story in stories.find():
        tags = story["tags"]
        for tag in tags:
            taglist.add(tag)

    storylist = stories.find()
    return render_template('index.html', storylist=storylist, taglist=taglist)


@base.route('/create_story', methods=['POST'])
def create_story():

    stories.insert_one(request.form.to_dict(flat=False))
    return redirect(url_for('base.story_page'))


@base.route('/profile')
@login_required
def profile():

    return render_template("profile.html", name=current_user.username)
