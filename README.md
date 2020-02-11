# Project Overview


## Project Description

Creating an auto swap site that allow dealers or private sellers submit cars for sale.

## Project Links
The github repo is at the following location.


- [https://github.com/mh44698/Auto-swap]()


## Components

- Header -- Provide links to the various pages.
- Home -- The Cars listing page.
-	view Cars -- The Car listing page.
- View Sellers -- The Seller listing page.
-	Car Detail --	Provide the detail view of an individual car.
-	Seller Detail -- Provide the detail view of the seller and a list of cars they currenlty have on the site.
-	Create/Update -- Allows a user to create and or update a car or a seller.
-	Delete - Allows a user to delete a car or a seller from the site.



## Installation Instructions

Clone the code from the GitHub repositories above.
	the virtual environment is not included in the repo so you will need to set it up.
		> python3 -m venv .env
		> source .env/bin/activate

	Install Django and pyscopg2-binary and Pillow
		Installed Pillow to help with the image uplader.

	The database you will need to create locally is:
		DATABASES = {
				'default': {
						'ENGINE': 'django.db.backends.postgresql_psycopg2',
						'NAME': 'auto',
						'USER': 'autouser',
						'PASSWORD': 'auto',
						'HOST': 'localhost',
				}
		}

The models are created for you and there is a migration file with seed data that will create and update your tables.
	
	-	0001_initial.py
	-	0002_auto_20200211_1726.py


WIP
Working on linking a css view to enhance the styling
	-	Started the the css file with some formating and sytling
	
working on implementing an image uploader for the individual cars
	I was able to get an image to show up if the image URL was in the database however; when I tried to add a new one it was not accepting the url format.  Due to this I started looking into creating an image uploaded.  I have a form created called upload_pic.hmtl.  Add the imageuploader in the forms.py file and added a path to the urls.py file and created a view.  However, the view is not render the form properly.  I used the following site as a reference:

###
-	[https://www.programcreek.com/python/example/52376/django.http.HttpResponseForbidden]()
-	[https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield]()

I used this site up update the database model to a URLField type:
- [https://docs.djangoproject.com/en/dev/ref/models/fields/#imagefield]()



Future
Would like to add social athentication 
Limit user permission on create and edit pages
Would need to create a record after they have a user created and they would only be able to edit their own pages.



## Code Snippet
### CSS Issues ###


### Resolution ###


### Testing Issue ###

### Resolution ###


 