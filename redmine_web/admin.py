from django.contrib import admin
from redmine_web.models import People
from redmine_web.models import Ariticle, Comment

# Register your models here.

admin.site.register(People)
admin.site.register(Ariticle)
admin.site.register(Comment)