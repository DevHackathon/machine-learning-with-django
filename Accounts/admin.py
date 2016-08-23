from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Account

user = get_user_model()

class AccountInline(admin.StackedInline):
		model = Account
		can_delete = False

class AccountAdmin(UserAdmin):
		inlines = (AccountInline,)

admin.site.unregister(user)
admin.site.register(get_user_model(), AccountAdmin)