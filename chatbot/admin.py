from django.contrib import admin
from .models import Intent, Response, UserInput

admin.site.register(Intent)
admin.site.register(Response)
admin.site.register(UserInput)
