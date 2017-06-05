=====
News
=====

News is a simple Django app to create and publish short news feeds.

Quick start
-----------

1. Add "news" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'news',
    ]

2. Run `python manage.py migrate` to create the news models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a newsfeed (you'll need the Admin app enabled).

4. Display the news entries in any template by using the template tag:

    {% newsfeed_last_items %}
