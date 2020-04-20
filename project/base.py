from flask import (Blueprint, current_app, render_template, url_for, request,
                   redirect)
from flask_login import login_required, current_user
from .extensions import mongo
from bson.objectid import ObjectId

base = Blueprint('base', __name__,
                 template_folder='templates')

stories = mongo.db.stories
story_list = stories.find()


def get_tags():

    taglist = current_app.config['taglist']

    for story in story_list:
        tags = story["tags"]
        for tag in tags:
            taglist.add(tag)

    return taglist


@base.route('/')
def story_page():

    taglist = get_tags()

    if current_user.is_authenticated:
        return render_template('index.html', story_list=story_list,
                               taglist=taglist, username=current_user.username)

    return render_template('index.html', story_list=story_list,
                           taglist=taglist)


@base.route('/create_story', methods=['POST'])
def create_story():

    stories.insert_one(request.form.to_dict(flat=False))
    return redirect(url_for('base.story_page'))


@base.route('/profile')
@login_required
def profile():

    user_stories = stories.find({'username': current_user.username})

    taglist = get_tags()

    return render_template("profile.html", username=current_user.username,
                           user_stories=user_stories, taglist=taglist)


@base.route('/edit_story/<story_id>', methods=["POST"])
@login_required
def edit_story(story_id):
    stories.update({'_id': ObjectId(story_id)},
                   {'$set':
                    {
                        "first_name.0": request.form.get('first_name'),
                        'last_name.0': request.form.get('last_name'),
                        'age.0': request.form.get('age'),
                        'country.0': request.form.get('country'),
                        'language.0': request.form.get('language'),
                        'date.0': request.form.get('date'),
                        'tags': request.form.getlist('tags[]'),
                        'color.0': request.form.get('color'),
                        'title.0': request.form.get('title'),
                        'text.0': request.form.get('text'),
                    }
                    })

    return redirect(url_for('base.profile'))
