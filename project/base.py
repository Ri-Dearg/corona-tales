from flask import (Blueprint, current_app, render_template, url_for, request,
                   redirect, flash, jsonify)
from flask_login import login_required, current_user
from .extensions import mongo, mail
from config import ADMINS
from flask_mail import Message
from bson.objectid import ObjectId
import time
import calendar
# Used to paginate for Infinite Scroll
from flask_paginate import Pagination, get_page_args

base = Blueprint('base', __name__,
                 template_folder='templates')

stories = mongo.db.stories  # Database for story posts
users = mongo.db.users  # Database for users
mailapp = mail


def get_tags():
    """Used to recieve tags from all stories and
    create an autocomplete list."""
    taglist = current_app.config['taglist']

    for story in stories.find({}, {'tags': 1}):
        tags = story['tags']
        for tag in tags:
            taglist.add(tag)

    return taglist


def paginate(array, page, offset=0, per_page=10):
    """Creates an ordered list with details for pagination."""
    offset = (page-1) * 7  # Stories to display per page]
    return array[offset: offset + per_page]

# ---------------------------------------------------------------------
# Index Page
# ---------------------------------------------------------------------
@base.route('/')
def story_page():
    """Generates the content for the index page. Creates an iterable which
    pushes featured stories to the top, followed by other stories. Paginates
    the content for use by Infinite Scroll."""
    # Sorts order by newest post first
    story_list = stories.find().sort('time', -1)
    story_array = []  # story_list to be paginated
    index = 0  # used to limit story_list

    for story in story_list:
        if story['featured']:  # psuhes featured stories first
            story_array.append(story)
    story_list.rewind()  # Resets iterable to push normal stories second

    for index, story in zip(range(100), story_list):
        if not story['featured']:
            story_array.append(story)

    taglist = get_tags()

    # sets srgument names for pagination
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    # runs functions to get stories and paginate them
    pagination_stories = paginate(story_array, page=page, offset=offset,
                                  per_page=7)
    total = story_list.count()
    pagination = Pagination(page=page, per_page=7, total=total)

    return render_template('index.html', taglist=taglist,
                           base_story_list=pagination_stories, page=page,
                           per_page=per_page, pagination=pagination)


@base.route('/create_story', methods=['POST'])
def create_story():
    """Adds a story document to the database. Attaches the user ID if they
    are logged in. Every story gets one like on creation, my like. :-)"""

    tag_values = []
    for tag in request.form.getlist('tags'):
        no_space = tag.split(' ')
        for new_tag in no_space:
            clean_tag = new_tag.lstrip('#')
            tag_values.append(clean_tag)

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
                            'likes': 1,
                            'tags': tag_values})

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
                            'likes': 1,
                            'tags': tag_values})

    flash('your story has been posted!', 'success')
    return redirect(request.referrer)


# ---------------------------------------------------------------------
# Profile Page
# ---------------------------------------------------------------------
@base.route('/profile')
@login_required
def profile():
    """Renders the profile page for authenticated users, searching the
    database for all stories written by the user"""
    story_list = stories.find(
        {'user_id': current_user.user_id}).sort('time', -1)
    username = current_user.username

    user_array = []
    for story in story_list:
        user_array.append(story)

    # Paginate results
    taglist = get_tags()
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    pagination_user = paginate(
        user_array, page=page, offset=offset, per_page=7)
    total = story_list.count()
    pagination = Pagination(page=page, per_page=7, total=total)

    return render_template('profile.html', edit_story_list=pagination_user,
                           taglist=taglist, page=page, per_page=per_page,
                           pagination=pagination, username=username)


@base.route('/fill_info', methods=['POST'])
@login_required
def fill_info():
    """Saves information in an embedded document that automaticallly fills
    form fields for the user so if they want to write more stories, they don't
    have to repeat the info"""
    name_fill = request.form.get('name-fill')
    age_fill = request.form.get('age-fill')
    country_fill = request.form.get('country-fill')
    language_fill = request.form.get('language-fill')

    # If any info is entered, creates the document fields
    if name_fill or age_fill or country_fill or language_fill:
        users.update_one({'user_id': current_user.user_id},
                         {'$set':
                          {'prefill':
                           {'name': name_fill,
                            'age': age_fill,
                            'country': country_fill,
                            'story_language': language_fill, }}})

        flash('your details have been saved', 'success')
        return redirect(url_for('base.profile', _anchor='user-settings'))

    # if no information was entered, alerts the user.
    flash('please fill one field', 'sorry')
    return redirect(url_for('base.profile', _anchor='user-settings'))


@base.route('/delete_info', methods=['POST'])
@login_required
def delete_info():
    """Deletes the fields in the embedded document that saves info for
    prefilling forms"""
    users.update_one({'user_id': current_user.user_id},
                     {'$unset':
                      {'prefill.name': "",
                       'prefill.age': "",
                       'prefill.country': "",
                       'prefill.story_language': ""}})

    flash('saved info has been deleted', 'success')
    return redirect(url_for('base.profile', _anchor='user-settings'))


@base.route('/edit_story/<story_id>', methods=['POST'])
@login_required
def edit_story(story_id):
    """Updates user stories with edited details """

    tag_values = []
    for tag in request.form.getlist('tags'):
        no_space = tag.split(' ')
        for new_tag in no_space:
            clean_tag = new_tag.lstrip('#')
            tag_values.append(clean_tag)

    stories.update_one({'_id': ObjectId(story_id)},
                       {'$set':
                        {'name': request.form.get('name'),
                         'age': int(request.form.get('age')),
                         'country': request.form.get('country'),
                         'story_language': request.form.get('language'),
                         'tags': tag_values,
                         'color': request.form.get('color'),
                         'title': request.form.get('title'),
                         'text': request.form.get('text'),
                         'edit_time': int(time.time()*1000)}})

    return redirect(url_for('base.profile'))


@base.route('/delete_story/<story_id>', methods=['POST'])
@login_required
def delete_story(story_id):
    """Deletes a single story"""
    stories.remove({'_id': ObjectId(story_id)})

    flash('the story has been deleted.', 'success')
    return redirect(url_for('base.profile'))


@base.route('/like', methods=['POST'])
@login_required
def like():
    """Either saves a liked stories's objectID to an array in a user document,
    and increases the value of like field in the story document, or removes
    the objectid from the user document and decreases the like value. If the
    likes reaches 21 likes, the story is 'featured', and it will be shown at
    the top of the index page before other stories. The choice to not return
    featured to 'False' if unliked below 21 likes is deliberate. It then
    passes the number of likes back to the ajax function to display it to the
    user."""
    post_id = request.form.get('like-id')

    user_likes = (users.find_one({'user_id': current_user.user_id},
                                 {'liked': 1}))
    # Condition checks if the story is liked, removes it, lowering likes
    if ObjectId(post_id) in user_likes['liked']:
        users.update_one({'user_id': current_user.user_id},
                         {'$pull':
                          {'liked': ObjectId(post_id)}})

        stories.update_one({'_id': ObjectId(post_id)},
                           {'$inc':
                            {'likes': -1}})
    # Condition likes story, saving it to user document and increses likes
    if ObjectId(post_id) not in user_likes['liked']:
        users.update_one({'user_id': current_user.user_id},
                         {'$push':
                          {'liked': ObjectId(post_id)}})

        stories.update_one({'_id': ObjectId(post_id)},
                           {'$inc':
                            {'likes': 1}})

    # Gets story likes
    likes_number = stories.find_one({'_id': ObjectId(post_id)},
                                    {'likes': 1})

    likes_total = likes_number['likes']

    # Features stories with more than 21 likes
    if likes_total == 21:
        stories.update_one({'_id': ObjectId(post_id)},
                           {'$set': {'featured': True}})

    return jsonify(likes_total)


# ---------------------------------------------------------------------
# Search Page
# ---------------------------------------------------------------------
@base.route('/search', methods=['GET'])
def search():
    """Searches entire database for matching documents using a text index
    and int values, return the results."""
    def ranges(from_age, to_age, from_date, to_date, base_text, country,
               story_lang, tag_string):
        """Search function called if any int values are requested"""

        # Sets default values for ranges to extremes for int search
        # As the search contains ranges
        if from_age is None:
            from_age = 0

        if to_age is None:
            to_age = 120

        if from_date is None:
            from_date = 0

        if to_date is None:
            to_date = 9999999999999

        # Checks for text, if there is text in the search this condition runs
        if any(t is not None for t in [base_text, country, tag_string]):

            results = stories.find({
                'time': {'$gte': from_date, '$lte': to_date},
                'age': {'$gte': from_age, '$lte': to_age},
                '$text': {'$search': f'{base_text}\
                                    {country}\
                                    {story_lang}\
                                    {tag_string}'}},
                {'score': {'$meta': 'textScore'}}).sort(
                [('score', {'$meta': 'textScore'})])

        # Otherwise a search containing only ints runs
        else:
            results = stories.find({
                'time': {'$gte': from_date, '$lte': to_date},
                'age': {'$gte': from_age, '$lte': to_age},
            })

        return results

    taglist = get_tags()

    # sets all search values to none as default so the search can be carried
    # out no matter which fields are entered or left out
    base_text = None
    country = None
    story_lang = None
    tag_search = None
    tag_string = None

    from_age = None
    to_age = None
    from_date = None
    to_date = None

    # conditions check to see which values have been entered
    if request.args.get('search-text'):
        base_text = request.args.get('search-text')

    if request.args.get('search-country'):
        country = request.args.get('search-country')

    if request.args.get('search-language'):
        story_lang = request.args.get('search-language')

    if request.args.getlist('tags'):
        tag_search = request.args.getlist('tags')
        tag_string = ' '.join(tag_search)

    if request.args.get('search-age-f'):
        from_age = int(request.args.get('search-age-f'))

    if request.args.get('search-age-t'):
        to_age = int(request.args.get('search-age-t'))

    if request.args.get('search-date-f'):
        from_date = int(calendar.timegm(time.strptime(
            request.args.get('search-date-f'), '%b %d, %Y')))*1000

    if request.args.get('search-date-t'):
        to_date = int(calendar.timegm(time.strptime(
            request.args.get('search-date-t'), '%b %d, %Y')))*1000 + 86399999

    # if int ranges have been entered, runs ranges function
    if any(v is not None for v in [from_age, to_age, from_date, to_date]):
        results = ranges(from_age, to_age, from_date, to_date, base_text,
                         country, story_lang, tag_string)

    # otherwise it runs a text search
    else:
        results = stories.find({
            '$text': {'$search': f'{base_text} \
                                {country}\
                                {story_lang}\
                                {tag_string}'}},
            {'score': {'$meta': 'textScore'}}).sort(
            [('score', {'$meta': 'textScore'})])

    story_array = []

    # iterates through the results and checks for country and language
    # search. These values are entered into the text index for general
    # results, so they cannot be searched seperately, but must act as filters
    # so these conditions check different combinations and filters results
    for result in results:
        if any(v is not None for v in [country, story_lang]):
            if country is not None:
                if story_lang is not None:
                    if result['country'] == country and \
                       result['story_language'] == story_lang:
                        story_array.append(result)

                elif result['country'] == country:
                    story_array.append(result)

            elif result['story_language'] == story_lang:
                story_array.append(result)

        else:
            story_array.append(result)

    # paginates results for infinite scroll
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    pagination_results = paginate(story_array, page=page, offset=offset,
                                  per_page=7)
    total = len(story_array)
    pagination = Pagination(page=page, per_page=7, total=total)

    return render_template('search.html', base_story_list=pagination_results,
                           taglist=taglist, page=page, per_page=per_page,
                           pagination=pagination)


@base.route('/search_tags/<string:tag>', methods=['GET'])
def search_tags(tag):
    """Runs a simple tag search using the text index. Tags are weighted
    more important than general text in searches, so the results will arrive
    first. This general search is intended. May consider doing a specific tag
    search."""
    taglist = get_tags()

    results = stories.find({
        '$text': {'$search': f'{tag}'}},
        {'score': {'$meta': 'textScore'}}).sort(
        [('score', {'$meta': 'textScore'})])

    story_array = []

    for result in results:
        story_array.append(result)

    # paginate results
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    pagination_results = paginate(
        story_array, page=page, offset=offset, per_page=7)
    total = len(story_array)
    pagination = Pagination(page=page, per_page=7, total=total)

    return render_template('search.html', base_story_list=pagination_results,
                           taglist=taglist, page=page, per_page=per_page,
                           pagination=pagination)


# ---------------------------------------------------------------------
# Contact Page
# ---------------------------------------------------------------------
@base.route('/contact')
def contact():
    """Renders contatc page"""
    taglist = get_tags()

    return render_template('contact.html', taglist=taglist)


@base.route('/send_mail', methods=['POST'])
def send_mail():
    """Send a formatted email using flask-fail"""
    msg = Message('Corona-Tales Contact',
                  sender=request.form.get('email'),
                  recipients=[ADMINS])

    msg.html = f'<p>Message from <b>{request.form.get("email-name")}</b> at \
                <b>{request.form.get("email")}</b><br>\
                Tel: <b>{request.form.get("number")}</b></p>\
                <p>{request.form.get("message")}</p>'

    mailapp.send(msg)
    flash('your message has been sent.', 'success')
    return redirect(url_for('base.contact'))


# ---------------------------------------------------------------------
# About Page
# ---------------------------------------------------------------------
@base.route('/about')
def about():
    """Renders about page."""
    taglist = get_tags()

    return render_template('about.html', taglist=taglist)
