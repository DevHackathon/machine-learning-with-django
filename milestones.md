Requirements that this project aims to do
-----------------------------------------
1) User account.
	- Security/Privacy
		Registration of the user
		Authentication of the user
		Login/Logout of the user into the app
		Individual url for the user saved which will be unique
	- Account details and profile
		-Profile credentials with real firstname and last name
		-Username for posting any information to the feeds
		- Profile credentials
			* Gender
			* Age
			* location
		- Profile picture
		
2) Product.(apps)
		- picture[APP]
				- upload
				- delete
				- update{ 
						transformation picture: before_after
						}
		- Newsfeed section for the user below the picture
				- create Newsfeed
				- Retrieve Newsfeed
				- Update Newsfeed
				- Delete NewsFeed
			-Newsfeed fed through the Watson Api for a happiness threshhold.

					threshold_level[x]= 0.5, x:={positive, negative}
				- If newsfeed > threshold_level[negative]:
							Raise warning "Status does not abide by our happiness policy"
					elif newsfeed > threshold_level[positive]:
							print "smiley face"{ javascript smiley}
					else:
						pass
		-Date_added- Date added by the user
		-Date_updated - Date the user updates comments/ status post

		- comment section for the users to comment on:[APP]
					- bonus points for threading the comments
					- Create comment
					- Update Comment
					- Delete comment
					- Retrive comment
					- pass through watsons threshold_sentiment analysis 
					{
						most of these can be handled by django_comments
						 }
		


		- Data gotten from the user:[APP]
				- Data regarding the workout levels i.e
						1) Instance of workout - choiceField
						2) name of workout - choice Field
						3) weight done
						4) Date added
						5) reps
	** subject to change, additions and subtractions

	Tools to be used for this project:
		1) python-Django
		2) Javascript - Angular, D3js
		3) Google Charts
		4) deployment database - SQLITE3, 
		5) Production database - Postgresql maybe SQLITE if am feeling lazy
		6) Watson Sentiment Analysis.

WorkFlow:

	-start with the images/ newsfeed section
	-Create a home page of images preferrably tile based images
	- initialize the watson api .
	- Users
	- Data points.


