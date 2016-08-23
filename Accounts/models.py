from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Account(models.Model):
	"""docstring for Account"""
	user = models.OneToOneField(User, unique=True)
	age = models.IntegerField(default=18, null=False, blank=False)
	muting_value = models.FloatField(default=5.0) # this will be the value used to mute the noisey feeds

	def __str__(self):
			return "%s profile" %self.user

def create_profile(sender, instance, created, **kwargs):
			if created:
					profile, created = Account.objects.get_or_create(user=instance)
					