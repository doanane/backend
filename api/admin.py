from django.contrib import admin
from .models import *
from markdownx.admin import MarkdownxModelAdmin
    
# Register your models here.
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(ContactUs)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Gallery)
