from flask import (Blueprint, current_app, render_template, url_for, request,
                   redirect, flash)
from flask_login import login_required, current_user
from .extensions import mongo  # ASCENDING
from bson.objectid import ObjectId

base = Blueprint('base', __name__,
                 template_folder='templates')

stories = mongo.db.stories
story_list = stories.find().sort('time', -1)


def get_tags():

    taglist = current_app.config['taglist']

    for story in stories.find():
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

    flash('your story has been posted!', 'success')
    stories.insert_one({'user_id': request.form.get('user_id'),
                        'name': request.form.get('name'),
                        'age': request.form.get('age'),
                        'country': request.form.get('country'),
                        'story_language': request.form.get('language'),
                        'color': request.form.get('color'),
                        'title': request.form.get('title'),
                        'text': request.form.get('text'),
                        'time': request.form.get('time'),
                        'featured': False,
                        'tags': request.form.getlist('tags')})
    return redirect(request.referrer)


@base.route('/search', methods=['GET'])
def search():
    taglist = get_tags()

    results = stories.find({'$text':
                            {'$search': request.args.get('search-text')}})

    for result in results:
        print(results)

    return render_template('search.html', results=results, taglist=taglist)


@base.route('/about')
def about():

    taglist = get_tags()

    if current_user.is_authenticated:
        return render_template('about.html', taglist=taglist,
                               user_id=current_user.user_id)

    return render_template('about.html', taglist=taglist)


@base.route('/contact')
def contact():

    taglist = get_tags()

    if current_user.is_authenticated:
        return render_template('contact.html', taglist=taglist,
                               user_id=current_user.user_id)

    return render_template('contact.html', taglist=taglist)


@base.route('/profile')
@login_required
def profile():

    user_stories = stories.find(
        {'user_id': current_user.user_id}).sort('time', -1)
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
                        'name': request.form.get('name'),
                        'age': request.form.get('age'),
                        'country': request.form.get('country'),
                        'story_language': request.form.get('language'),
                        'tags': request.form.getlist('tags'),
                        'color': request.form.get('color'),
                        'title': request.form.get('title'),
                        'text': request.form.get('text'),
                        'edit_time': request.form.get('edit-time'),
                    }
                    })

    return redirect(url_for('base.profile'))


@base.route('/delete_story/<story_id>',)
@login_required
def delete_story(story_id):
    mongo.db.stories.remove({'_id': ObjectId(story_id)})

    return redirect(url_for('base.profile'))
