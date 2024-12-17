from django.contrib import admin
from users.models import Profile, ItemPictures, Cart

# Register your models here.

admin.site.register(Profile)
admin.site.register(ItemPictures)
admin.site.register(Cart)