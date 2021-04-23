ClinNotes
=========

## Demo Site
[ClinNotes](https://fierce-sierra-99431.herokuapp.com/)

## About
Clinnotes is a project designed to help clinicians (doctors, therapists ect) manage patient care through reflections and reminders they can tag to a patient's episode of care. As a clinician it is not uncommon to have patients who make visits infrequently for various reasons. If one is practicing in a clinical environment that is busy and hectic it can be difficult to recall all patient details prior to a scheduled appointment, thus harming quality of care. Ideally, looking back at past visit notes could easily solve this. However, clinicians are trained and incentivized to write these visit notes in a way that optimizes billing and minimizes risk of litigation. This does not equate to accurate or helpful reflection or note taking. This is compounded by the plethora of tasks clinicians must complete in addition to seeing between 15-30 patients daily in some instances. As a practicing physical therapist I often tried to solve this issue with post it notes, which for numerous reasons may not be ideal. ClinNotes was designed to make this process easier and more organized for patients.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/pydanny/cookiecutter-django/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## How it works:
- Clinician creates an account
- Clinician may create patients and episode of care on webapp
- Clinician has ability to create, access, update and delete reflections or reminders for a specific patient in a given care episode.
- Reflections relate to how the clinician may improve there ability to provide care
- Reminders relate to details that are relevant to specific patients
- Ideally the clinician can use the webapp as a quick refresher prior to a visit or as a way to reflect on patient care to improve abilities
- The clinician may upgrade to guided reflection access through a one time payment which will prompt the clinician with specific ideas or questions to reflect on (just a demo---you wont actually be charged)

## Tech Stack Used:
- Django
- Django all auth : https://django-allauth.readthedocs.io/en/latest/installation.html
- Stripe : https://stripe.com/docs
- Tailwind : https://tailwindcss.com/docs
- Django Cookie Cutter
- Tutorials from Matthew Freire were instrumental in learning stripe and tailwind to assist in development. : https://justdjango.com/

## How to run Locally: 
* create a virtial environment
* clone repository
* run pip install -r requirements/local.txt
* You will need postgres installed....create a postgres database via the following command (if not you can use SQLITE3):

```
$ createdb your_database_name_here
```

- Configure the postgres database for running application and tests ( inside psql)

```
    postgres=# CREATE USER your_username_here WITH PASSWORD 'your_password_here';

    postgres=# GRANT ALL PRIVILEGES ON DATABASE your_database_name_here TO your_username_here;
    
    postgres=# ALTER ROLE your_username_here CREATEDB;
 ```
    
    
* configure .env file (see .sample_dot_env_file)
* run migrations
* run server ( all-auth ( google and amazon login) and stripe will need additional configuration but the rest of the site will work )


**Setting Up Your Users**

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::
```
    $ python manage.py createsuperuser
```
For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.


Deployment
----------

## Heroku
- `cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html


## Reflection

### The Good/ My growth:
- Implementing DjangoAllAuth, allowing user to login via email and password only, rather than having to create a username.
- Social Authentication ability through Google or amazon as a login option.
- Integration of Stripe and Stripe webhooks for the ability to upgrade to expanded content on the app
- Heavy use of Class based views for less complex and more readable code
- Use of Django cookie cutter for more efficient development locally and in production
- Use of tailwind CSS for improved styling and more efficient development

### The Bad/Areas to improve:
- No test coverage during development
- I used Django cookie cutter for the first time during this project and found it very convenient and effective. However, I eventually discovered that is a great tool if and only if you understand everything it is doing for you. This caused me to struggle in future projects and modify my use for the time being





