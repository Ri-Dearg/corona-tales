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
                               taglist=taglist, user_id=current_user.user_id)

    return render_template('index.html', story_list=story_list,
                           taglist=taglist)


@base.route('/create_story', methods=['POST'])
def create_story():

    stories.insert_one(request.form.to_dict(flat=False))
    return redirect(url_for('base.story_page'))


@base.route('/about')
def about():

    return render_template('about.html')


@base.route('/contact')
def contact():

    return render_template('contact.html')


@base.route('/profile')
@login_required
def profile():

    user_stories = stories.find({'user_id': current_user.user_id})
    username = current_user.username

    # Change order of function when adding create story to profile page
    taglist = get_tags()

    return render_template("profile.html", user_id=current_user.user_id,
                           user_stories=user_stories, taglist=taglist,
                           username=username)


@base.route('/edit_story/<story_id>', methods=["POST"])
@login_required
def edit_story(story_id):
    stories.update({'_id': ObjectId(story_id)},
                   {'$set':
                    {
                        "name.0": request.form.get('name'),
                        'age.0': request.form.get('age'),
                        'country.0': request.form.get('country'),
                        'language.0': request.form.get('language'),
                        'tags': request.form.getlist('tags'),
                        'color.0': request.form.get('color'),
                        'title.0': request.form.get('title'),
                        'text.0': request.form.get('text'),
                        'edit_time.0': request.form.get('edit-time'),
                    }
                    })

    return redirect(url_for('base.profile'))


@base.route('/delete_story/<story_id>',)
@login_required
def delete_story(story_id):
    mongo.db.stories.remove({'_id': ObjectId(story_id)})

    return redirect(url_for('base.profile'))
