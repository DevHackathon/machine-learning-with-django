from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model

import json

from .models import PostFeed
from Accounts.models import Account
from .forms import PostFeedForm
# Create your views here.

user = get_user_model()

class PostFeedListView(ListView) :
		model = PostFeed
		template_name = "base.html"

		
		def get_context_data(self, **kwargs):
				context = super(PostFeedListView, self).get_context_data(**kwargs)
				queryset = PostFeed.objects.all()
				account = Account.objects.get(user = self.request.user)
				#setting the user muting property
				muting_value = account.muting_value
				# muting factor algorithm
				muting_factor = ((1/5)*muting_value) -1
				
				for query in queryset:
					if muting_factor >= query.sentiment_score:
							query.fail = True							
					else:
							query.fail = False
					query.save()

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
		success_url = '/'

		def form_valid(self, form):

				self.object = form.save(commit=False)
				self.object.is_published = True
				self.object.submitter = self.request.user
				unserialized_json = form.ask_watson()
				serialized_json = json.dumps(form.ask_watson(), sort_keys=True, indent=4)	
				# score value from the watson json sentiment analysis
				score_value = (unserialized_json["docSentiment"]["score"])
				print (score_value)
				self.object.sentiment_score = float(score_value)
				# sample value for sentiment analysis[sanity check!] it works
			
				self.object.save()
				context = self.get_context_data()

				context = {
				"score" : score_value,
					}
				return super(FeedFormView, self).form_valid(form)
