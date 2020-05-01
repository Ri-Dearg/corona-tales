from flask import (Blueprint, current_app, render_template, url_for, request,
                   redirect, flash, jsonify)
from flask_login import login_required, current_user
from .extensions import mongo, mail
from config import ADMINS
from flask_mail import Message
from bson.objectid import ObjectId
import time
import calendar
import pprint
from flask_paginate import Pagination, get_page_args

base = Blueprint('base', __name__,
                 template_folder='templates')

stories = mongo.db.stories

mailapp = mail

story_array = []


def like_check():
    user_likes = (mongo.db.users.find_one({'user_id': current_user.user_id},
                                          {'liked': 1}))
    return jsonify(user_likes['liked'])


def get_tags():

    taglist = current_app.config['taglist']

    for story in stories.find():
        tags = story["tags"]
        for tag in tags:
            taglist.add(tag)

    return taglist


@base.route('/')
def story_page():

    story_list = stories.find().sort('time', -1)

    def get_stories(page, offset=0, per_page=10):
        story_array = []
        offset = (page-1) * 7
        for story in story_list:
            story_array.append(story)
        return story_array[offset: offset + per_page]

    taglist = get_tags()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    pagination_stories = get_stories(page=page, offset=offset,
                                     per_page=7)
    total = story_list.count()
    pagination = Pagination(page=page, per_page=7,
                            total=total)

    return render_template('index.html',
                           taglist=taglist, story_list=pagination_stories,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


@base.route('/create_story', methods=['POST'])
def create_story():
    if current_user.is_authenticated:
        stories.insert_one({'user_id': current_user.user_id,
                            'name': request.form.get('name'),
                            'age': int(request.form.get('age')),
                            'country': request.form.get('country'),
                            'story_language': request.form.get('language'),
                            'color': request.form.get('color'),
                            'title': request.form.get('title'),
                            'text': request.form.get('text'),
                            'time': int(time.time()*1000),
                            'featured': False,
                            'likes': 0,
                            'tags': request.form.getlist('tags')})

    else:
        stories.insert_one({'name': request.form.get('name'),
                            'age': int(request.form.get('age')),
                            'country': request.form.get('country'),
                            'story_language': request.form.get('language'),
                            'color': request.form.get('color'),
                            'title': request.form.get('title'),
                            'text': request.form.get('text'),
                            'time': int(time.time()*1000),
                            'featured': False,
                            'tags': request.form.getlist('tags')})

    flash('your story has been posted!', 'success')
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
                                    {country} \
                                    {story_lang} \
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

    if request.args.get('search-age-f'):
        from_age = int(request.args.get('search-age-f'))

    if request.args.get('search-age-t'):
        to_age = int(request.args.get('search-age-t'))

    if request.args.get('search-date-f'):
        from_date = int(calendar.timegm(time.strptime(
            request.args.get('search-date-f'), "%b %d, %Y")))*1000

    if request.args.get('search-date-t'):
        to_date = int(calendar.timegm(time.strptime(
            request.args.get('search-date-t'), "%b %d, %Y")))*1000 + 86399999

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

    story_list = []

    for result in results:

        if any(v is not None for v in [country, story_lang]):
            if country is not None:
                if story_lang is not None:
                    if result['country'] == country and \
                       result['story_language'] == story_lang:
                        story_list.append(result)

                elif result['country'] == country:
                    story_list.append(result)

            elif result['story_language'] == story_lang:
                story_list.append(result)

        else:
            story_list.append(result)

    def search_scroll(page, offset=0, per_page=10):
        offset = (page-1) * 7

        return story_list[offset: offset + per_page]

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    pagination_results = search_scroll(page=page, offset=offset,
                                       per_page=7)
    total = len(story_list)
    pagination = Pagination(page=page, per_page=7,
                            total=total)

    return render_template('search.html', story_list=pagination_results,
                           taglist=taglist,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


@base.route('/search_tags/<string:tag>', methods=['GET'])
def search_tags(tag):

    taglist = get_tags()

    results = stories.find({
        '$text': {'$search': f'{tag}'}},
        {'score': {'$meta': 'textScore'}}).sort(
        [('score', {'$meta': 'textScore'})])

    story_list = []

    for result in results:
        story_list.append(result)

    def search_scroll(page, offset=0, per_page=10):
        offset = (page-1) * 7

        return story_list[offset: offset + per_page]

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    pagination_results = search_scroll(page=page, offset=offset,
                                       per_page=7)
    total = len(story_list)
    pagination = Pagination(page=page, per_page=7,
                            total=total)

    return render_template('search.html', story_list=pagination_results,
                           taglist=taglist,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


@base.route('/about')
def about():

    taglist = get_tags()

    return render_template('about.html', taglist=taglist)


@base.route('/contact')
def contact():

    taglist = get_tags()

    return render_template('contact.html', taglist=taglist)


@base.route('/send_mail', methods=['POST'])
def send_mail():
    msg = Message("Corona-Tales Contact",
                  sender=request.form.get('email'),
                  recipients=[ADMINS])

    msg.html = f'<p>Message from <b>{request.form.get("email-name")}</b> at \
                <b>{request.form.get("email")}</b><br>\
                Tel: <b>{request.form.get("number")}</b></p>\
                <p>{request.form.get("message")}</p>'

    mailapp.send(msg)
    flash('your message has been sent.', 'success')
    return redirect(url_for('base.contact'))


@base.route('/profile')
@login_required
def profile():

    story_list = stories.find(
        {'user_id': current_user.user_id}).sort('time', -1)
    username = current_user.username

    def user_pages(page, offset=0, per_page=10):
        user_array = []
        offset = (page-1) * 7
        for story in story_list:
            user_array.append(story)
        return user_array[offset: offset + per_page]

    taglist = get_tags()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    pagination_user = user_pages(page=page, offset=offset,
                                 per_page=7)
    total = story_list.count()
    pagination = Pagination(page=page, per_page=7,
                            total=total)

    return render_template("profile.html",
                           story_list=pagination_user, taglist=taglist,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           username=username)


@base.route('/fill_info', methods=['POST'])
@login_required
def fill_info():

    name_fill = request.form.get('name-fill')
    age_fill = request.form.get('age-fill')
    country_fill = request.form.get('country-fill')
    language_fill = request.form.get('language-fill')

    if name_fill or age_fill or country_fill or language_fill:
        mongo.db.users.update_one({'user_id': current_user.user_id},
                                  {'$set':
                                   {'prefill': {'name': name_fill,
                                                'age': age_fill,
                                                'country': country_fill,
                                                'story_language': language_fill,
                                                }
                                    }
                                   })

        flash('your details have been saved', 'success')
        return redirect(url_for('base.profile', _anchor='user-settings'))

    flash('please fill one field', 'sorry')
    return redirect(url_for('base.profile', _anchor='user-settings'))


@base.route('/delete_info', methods=['POST'])
@login_required
def delete_info():
    mongo.db.users.update_one({'user_id': current_user.user_id},
                              {'$unset':
                               {'prefill.name': "",
                                'prefill.age': "",
                                'prefill.country': "",
                                'prefill.story_language': ""}})

    flash('saved info has been deleted', 'success')
    return redirect(url_for('base.profile', _anchor='user-settings'))


@base.route('/edit_story/<story_id>', methods=["POST"])
@login_required
def edit_story(story_id):
    stories.update_one({'_id': ObjectId(story_id)},
                       {'$set':
                        {
                            'name': request.form.get('name'),
                            'age': int(request.form.get('age')),
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


@base.route('/delete_story/<story_id>')
@login_required
def delete_story(story_id):
    stories.remove({'_id': ObjectId(story_id)})

    return redirect(url_for('base.profile'))


@base.route('/like', methods=['POST'])
@login_required
def like():
    print('hello')
    post_id = request.form.get('like-id')

    user_likes = (mongo.db.users.find_one({'user_id': current_user.user_id},
                                          {'liked': 1}))

    if ObjectId(post_id) in user_likes['liked']:
        mongo.db.users.update_one({'user_id': current_user.user_id},
                                  {'$pull':
                                   {'liked': ObjectId(post_id)
                                    }
                                   })

        stories.update_one({'_id': ObjectId(post_id)},
                           {'$inc':
                            {'likes': -1}
                            })

    if ObjectId(post_id) not in user_likes['liked']:
        mongo.db.users.update_one({'user_id': current_user.user_id},
                                  {'$push':
                                   {'liked': ObjectId(post_id)
                                    }
                                   })

        stories.update_one({'_id': ObjectId(post_id)},
                           {'$inc':
                            {'likes': 1}
                            })

    likes_number = stories.find_one({'_id': ObjectId(post_id)},
                                    {'likes': 1})

    likes_total = likes_number['likes']

    return jsonify(likes_total)
