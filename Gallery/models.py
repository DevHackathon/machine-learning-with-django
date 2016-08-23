from __future__ import unicode_literals

from django.db import models


# Create your models here.
class PostFeed(models.Model):
		'''
		This will have all the items that are needed to create a simple post feed that will eventually go with the image 
		that is added to the front page. It will have:

			newsfeed = The content OP wants everyone to see
			slug = the sluggification of the newsfeed content
			is_published =  has the post been published
			created_on =  when the post was initially created
			updated_on = if the post was updated/edited, this will record the timestamp of that.

		'''

		newsfeed = models.CharField(max_length=250, null=False, blank=False)
		slug = models.SlugField(max_length=250)
		is_published = models.BooleanField(default= False)
		created_on = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)
		updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)
		sentiment_score = models.IntegerField()

		class Meta:
				ordering = ['-created_on']
				verbose_name_plural = 'Post Feeds'

		def __str__(self):

				return self.newsfeed

