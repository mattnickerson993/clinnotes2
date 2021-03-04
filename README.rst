clinnotes
=========

Clinnotes is a project designed to help clinicians (doctors, therapists ect) manage patient care through reflections and reminders
they can tag to a patients episode of care.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

About the Project
^^^^^^^^^^^^^^^^^^^^^
Project is built with Django and uses Django allauth for authentication, including option for social authentication with google or amazon. Stripe
is used for processing payments for upgrading to additional features. CSS tailwind is used for styling. Django cookie cutter was used to build project.


Django all auth : https://django-allauth.readthedocs.io/en/latest/installation.html

Stripe : https://stripe.com/docs

Tailwind : https://tailwindcss.com/docs

Tutorials from Matthew Freire were instrumental in learning stripe and tailwind to assist in development. : https://justdjango.com/

If you'd like to run the project locally
^^^^^^^^^^^^^^^^^^^^^
* create a virtial environment
* clone repository
* run pip install -r requirements/local.txt
* create a postgres database via the following commands::
    $ createdb your_database_name_here

    $ CREATE USER your_username_here WITH PASSWORD 'your_password_here';

    $ GRANT ALL PRIVILEGES ON DATABASE your_database_name_here TO your_username_here;
    
* configure .env file (see .sample_dot_env_file)
* run migrations
* run server ( all-auth ( google and amazon login) and stripe will need additional configuration but the rest of the site will work )


Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy clinnotes

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html




