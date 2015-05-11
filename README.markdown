Having a model like below

    from django.contrib.auth.models import User # has migrations in 1.7

    class MyProxyUser(User):
        class Meta:
            proxy = True

in an app without migrations gives the following error when running the tests:

    django.db.migrations.state.InvalidBasesError: Cannot resolve bases for [<ModelState: 'django_proxy_model_problems.MyProxyUser'>]
    This can happen if you are inheriting models from an app with migrations (e.g. contrib.auth)
     in an app with no migrations; see https://docs.djangoproject.com/en/1.7/topics/migrations/#dependencies for more

Having read both

* https://docs.djangoproject.com/en/1.8/topics/migrations/#dependencies 
* https://docs.djangoproject.com/en/1.8/topics/db/models/#proxy-models

I can't figure out what I should be doing to resolve this problem (`manage.py makemigrations` reports `No changes detected`)

The problem can be reproduced by running `tox -e py27-django17`

This can be reproduced with Django 1.7 &amp; 1.8, but works fine with 1.4
