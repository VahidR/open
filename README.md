==============================
Open: A URL Shortening Service
==============================

Open is a URL shortening service that respects your Digital Civil Liberties.


Introduction
------------
Open is in alpha state. Pleas join this project and make it an open URL shortening service.
Here is the first impression:

![home](https://raw.github.com/vahidR/open/master/open/static/img/open.jpg)


Installation
------------
Fist clone it form github:
```bash
$ git clone git@github.com:vahidR/open.git open
```

Now you can have different options based on your perspective. 
You can observe the platform from three different point of view: `development`, `testing and Q&A` and `production`.
You can decide among these options based on the `settings` target that you specify.

If you would like to see it as `development` environment, issue the following command:
```bash
cd open/open
python manage.py syncdb --settings=open.settings.local
python manage.py runserver
```

Or from `testing` view point:
```bash
cd open/open
python manage.py syncdb --settings=open.settings.test
python manage.py test --settings=open.settings.test
```
* PS. You should see that one test is not passed. This is purposefully for completing the whole integration test..


The `production` mode has the same procedure.. only change the settings target to `--settings=open.settings.production`



TODO
----
* Complete the Integration test phase



