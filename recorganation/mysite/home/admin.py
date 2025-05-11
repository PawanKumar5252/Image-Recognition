from django.contrib import admin

from home.models import Users
from home.models import Category
from home.models import Session
from home.models import Categoryvideo

# Register your models here.


admin.site.register(Users)
admin.site.register(Category)
admin.site.register(Categoryvideo)

admin.site.register(Session)