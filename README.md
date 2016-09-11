# Open résumé

Open résumé is a simple online curriculum vitæ manager designed to integrate into your personnal website. The usage is intended to be simple : fill your profile with contact informations, your studies, your skills, your hobbies and you get a complete online professionnal profile.

It also aims to let you generate PDF version of your online résumé using LaTeX and let you write motivation letters directly into the website.

**Note:** Open résumé is still in early development stage.

## Setup development server

The project uses Python 3.4 and Django 1.8. Depending on your distribution, you may need to replace all `python` commands below by `python3.4`.

 1. clone the project: `git clone https://github.com/AugierLe42e/open-resume.git`
 2. install python 3.4
 3. install django 1.8 : `pip3.4 install django==1.8` or just `pip install django==1.8` (you may need to prefix with `sudo`, depending on your distribution)
 4. go to the project directory and run the DB migrations: `./manage.py migrate`
 5. create an admin user `./manage.py createsuperuser`
 6. install the proper bower packages:  `./manage.py bower install`
 7. start the server: `./manage.py runserver`
 8. go to `http://127.0.0.1:8000/admin`, connect yourself with user credential defined on step 5 and fill a profile
 9. go to `http://127.0.0.1:8000` and admire the result.
