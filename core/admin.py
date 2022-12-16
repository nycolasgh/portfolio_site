from django.contrib import admin
from .models import *

# Register your models here.
# from sitealto.core.models import About, Service, RecentWork, Client, Feedbacks

admin.site.register(About)
admin.site.register(Service)
admin.site.register(RecentWork)
admin.site.register(Client)
admin.site.register(Feedbacks)
