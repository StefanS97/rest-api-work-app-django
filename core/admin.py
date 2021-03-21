from django.contrib import admin
from .models import User, Industry, Region, JobOffer


admin.site.register(User)
admin.site.register(Industry)
admin.site.register(Region)
admin.site.register(JobOffer)
