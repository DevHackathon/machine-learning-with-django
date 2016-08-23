from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.shortcuts import get_object_or_404

import json

from .models import PostFeed
from .forms import PostFeedForm
# Create your views here.

class PostFeedListView(ListView) :
		model = PostFeed
		template_name = "base.html"

		def get_context_data(self, **kwargs):
				context = super(PostFeedListView, self).get_context_data(**kwargs)
				queryset = PostFeed.objects.all()
				context['posts'] = queryset
				return context

class FeedFormView(CreateView):
		'''
		attrs[
			form = PostFeedForm
			template_name ='feeds/forms.html'
			success_url = '.'
		]
		We are saving the model form as well as implementing the score of the form into the db. This begins also begins the muting of vulgar comments via a range scale
		'''

		form_class = PostFeedForm
		template_name = 'feeds/forms.html'
		success_url = '.'

		def form_valid(self, form):
				self.object = form.save(commit=False)
				self.object.is_published = True
				unserialized_json = form.ask_watson()
				serialized_json = json.dumps(form.ask_watson(), sort_keys=True, indent=4)	
				# score value from the watson json sentiment analysis
				score_value = (unserialized_json["docSentiment"]["score"])
				# sample value for sentiment analysis[sanity check!] it works
				if float(score_value)< 0: 
						print ("score is too small, it is advisable you dont view it")
				print(serialized_json)
				print (self.object)
				self.object.save()
				
				return HttpResponse(serialized_json, content_type="application/json")
