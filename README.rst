=====
News
=====

News is a simple Django app to create and publish short news feeds.

Quick start
-----------

1. Copy the news folder to your project

2. Add "news" to your INSTALLED_APPS setting like this:

    INSTALLED_APPS = [
        ...
        'news',
    ]

3. Run `python manage.py migrate` to create the news models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a newsfeed (you'll need the Admin app enabled).

5. Display the news entries in any template:

Add {% load news_extras %} to the top of the template.

To show the news: {% newsfeed_last_items %}
