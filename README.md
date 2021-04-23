ClinNotes
=========

## About
Clinnotes is a project designed to help clinicians (doctors, therapists ect) manage patient care through reflections and reminders they can tag to a patient's episode of care. As a clinician it is not uncommon to have patients who make visits infrequently for various reasons. If one is practicing in a clinical environment that is busy and hectic it can be difficult to recall all patient details prior to a scheduled appointment, thus harming quality of care. Ideally, looking back at past visit notes could easily solve this. However, clinicians are trained and incentivized to write these visit notes in a way that optimizes billing and minimizes risk of litigation. This does not equate to accurate or helpful reflection or note taking. This is compounded by the plethora of tasks clinicians must complete in addition to seeing between 15-30 patients daily in some instances. As a practicing physical therapist I often tried to solve this issue with post it notes, which for numerous reasons may not be ideal. ClinNotes was designed to make this process easier and more organized for patients.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/pydanny/cookiecutter-django/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

##How it works:
- Clinician creates an account
- Clinician may create patients and episode of cares on webapp
- Clinician has ability to create, access, update and delete reflections or reminders for a specific patient in a given care episode.
- Reflections related to how the clinician may improve there ability to provide care
- Reminders related details that are relevant to a specific patients
- Ideally the clinician can use the webapp as a quick refresher to prior to a visit or as a way to reflect on patient care to improve abilities
- The clinician may upgrade to  guided reflection access through a one time payment which will prompt the clinician with specific ideas or questions to reflect on (just a demo---you wont actually be charged)


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




