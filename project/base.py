from flask import (Blueprint, current_app, render_template, url_for, request,
                   redirect, flash)
from flask_login import login_required, current_user
from .extensions import mongo
from bson.objectid import ObjectId
import time
import calendar

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

    print(calendar.timegm(time.strptime("Jan, 15 2018", "%b, %d %Y")))

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
                        'age': int(request.form.get('age')),
                        'country': request.form.get('country'),
                        'story_language': request.form.get('language'),
                        'color': request.form.get('color'),
                        'title': request.form.get('title'),
                        'text': request.form.get('text'),
                        'time': int(time.time()*1000),
                        'featured': False,
                        'tags': request.form.getlist('tags')})
    return redirect(request.referrer)


@base.route('/search', methods=['GET'])
def search():

    def ranges(from_age, to_age, from_date, to_date, base_text, country,
               story_lang, tag_string):

        if from_age is None:
            from_age = 0

        if to_age is None:
            to_age = 120

        if from_date is None:
            from_date = 0

        if to_date is None:
            to_date = 9999999999999

        print(from_age, to_age, from_date, to_date)

        if any(v is not None for v in [base_text, country, tag_string]):

            results = stories.find({
                'time': {'$gte': from_date, '$lte': to_date},
                'age': {'$gte': from_age, '$lte': to_age},
                '$text': {'$search': f'{base_text} \
                                    {country}\
                                    {story_lang}\
                                    {tag_string}'}},
                {'score': {'$meta': 'textScore'}}).sort(
                [('score', {'$meta': 'textScore'})])

        else:
            results = stories.find({
                'time': {'$gte': from_date, '$lte': to_date},
                'age': {'$gte': from_age, '$lte': to_age},
            })

        return results

    taglist = get_tags()

    base_text = None
    country = None
    story_lang = None
    tag_search = None
    tag_string = None

    from_age = None
    to_age = None
    from_date = None
    to_date = None

    if request.args.get("search-text"):
        base_text = request.args.get("search-text")

    if request.args.get("search-country"):
        country = request.args.get("search-country")

    if request.args.get("search-language"):
        story_lang = request.args.get("search-language")

    if request.args.getlist("tags"):
        tag_search = request.args.getlist("tags")
        tag_string = ' '.join(tag_search)
        print(tag_search, tag_string)

    if request.args.get('search-age-f'):
        from_age = int(request.args.get('search-age-f'))

    if request.args.get('search-age-t'):
        to_age = int(request.args.get('search-age-t'))

    if request.args.get('search-date-f'):
        from_date = int(calendar.timegm(time.strptime(
            request.args.get('search-date-f'), "%b %d, %Y")))*1000

    if request.args.get('search-date-t'):
        to_date = int(calendar.timegm(time.strptime(
            request.args.get('search-date-t'), "%b %d, %Y")))*1000

    if any(v is not None for v in [from_age, to_age, from_date, to_date]):
        results = ranges(from_age, to_age, from_date, to_date, base_text,
                         country, story_lang, tag_string)

    else:
        results = stories.find({
            '$text': {'$search': f'{base_text} \
                                {country}\
                                {story_lang}\
                                {tag_string}'}},
            {'score': {'$meta': 'textScore'}}).sort(
            [('score', {'$meta': 'textScore'})])

    final_results = []

    for result in results:

        if any(v is not None for v in [country, story_lang]):
            if country is not None:
                if story_lang is not None:
                    if result['country'] == country and \
                       result['story_language'] == story_lang:
                        final_results.append(result)

                elif result['country'] == country:
                    final_results.append(result)

            elif result['story_language'] == story_lang:
                final_results.append(result)

        else:
            final_results.append(result)

    return render_template('search.html', final_results=final_results,
                           taglist=taglist)


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
                        'edit_time': int(time.time()*1000)
                    }
                    })

    return redirect(url_for('base.profile'))


@base.route('/delete_story/<story_id>',)
@login_required
def delete_story(story_id):
    mongo.db.stories.remove({'_id': ObjectId(story_id)})

    return redirect(url_for('base.profile'))
