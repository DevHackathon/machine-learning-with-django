from django import forms
from .models import PostFeed
from django.conf import settings

#watson Dependencies
import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1

# Get APIKEY from the settings
APIKEY = getattr(settings, "APIKEY", None)

# Watson authentication
alchemy_language = AlchemyLanguageV1(api_key=APIKEY)
class PostFeedForm(forms.ModelForm):

		class Meta:
				model = PostFeed
				fields = ['newsfeed']


		def ask_watson(self):
				newsfeed = self.cleaned_data.get("newsfeed")
				combined_operations = ['doc-sentiment']
				return alchemy_language.combined(text=newsfeed, extract=combined_operations)

		# def save(self, commit=True):
		# 		newsfeed = super(PostFeedForm, self).save(commit=False)
		# 		if commit:
		# 				newsfeed.save()
		# 		return newsfeed
