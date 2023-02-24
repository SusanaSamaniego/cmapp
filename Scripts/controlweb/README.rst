=====
cpanel
=====

 cpanel is a simple Django app to conduct Web-based cpanel. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "cpanel" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'cpanel',
    )

2. Include the basejob URLconf in your project urls.py like this::

    url(r'^cpanel/', include('cpanel.urls')),

3. Run `python manage.py migrate` to create the cpanelb models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a sociedadjob (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/cpanelb/ to participate in the cpanel.