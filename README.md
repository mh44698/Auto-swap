# Project Overview


## Project Description

Creating an auto swap site that allow dealers or private sellers submit cars for sale.

## Project Links
The github repo is at the following location.


- [https://github.com/mh44698/Auto-swap]()


## Components

- Header -- Provide the user with links to create, browse, about us and back to home throughout the application. 
- Home -- The landing page for the application.  Presents the user with a browse the existing ideas or create a new one.
-	TitleView --  A place to view all of the existing ideas. From here the user can add, update, or delete an idea.
- FullCard -- Present the user with the full details of the idea.
-	Create --	Provide the user a place to add a new idea to the site.
-	Update -- Allow the user to update an existing idea. 	 
-	Delete -- Allow the user to delete an idea.  
-	Login - Allows the user to create a user ID and password and then login 
- About Us -- Give an explaination of the site.



## Installation Instructions

Clone the code from the GitHub repositories above.
	the virtual environment is not included in the repo so you will need to set it up.
		> python3 -m venv .env
		> source .env/bin/activate

	Install Django and pyscopg2-binary

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


## Code Snippet
### CSS Issues ###


### Resolution ###


### Testing Issue ###

### Resolution ###


 