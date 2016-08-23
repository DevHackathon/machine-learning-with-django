from django.contrib import admin

# Register your models here.
from .models import PostFeed

class PostFeedAdmin(admin.ModelAdmin):

		list_display = ('__str__', 'is_published', 'created_on', 'updated_on',)

admin.site.register(PostFeed, PostFeedAdmin)