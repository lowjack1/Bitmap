# Bitmap (Django Implementation)<br />

## Technology Stack:
* Mysql
* Django Framework
* Python
* Html
* Css
* Javascript
* Jquery

## Make webapp functional:
Assuming Google Chrome and Python3 is installed in your system.
* Clone Bitmap repository in your home directory.
* Create virtual environment in <code> cd path/to/Bitmap-Django </code> <br />
`virtualenv .`
* Activate created virtualenv <br />
`source bin/activate`
* Install django in activated environment and other requirements <br />
`pip3 install -r requirements.txt` <br>
* Install MySQL server
* Create new schema or database <br />
`CREATE SCHEMA schema_name ;`
* Import data.sql file to the database. <br />
`mysql -u username -p database_name < path/to/Bitmap-Django/Data/gallery_bitmap_picgallery.sql`
* Update all the credentials of your database in `path/to/Bitmap-Django/Gallery/settings.py`
* Now propagate all changes in django project. <br />
`python3 manage.py collectstatic` <br />
`python3 manage.py makemigratiion` <br />
`python3 manage.py migrate` <br />
* Finally run the server. <br />
`pip3 manage.py runserver`
