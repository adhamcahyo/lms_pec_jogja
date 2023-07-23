from django.contrib import admin
from .models import Classroom

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'start_date', 'end_date')
    list_filter = ('instructor', 'start_date', 'end_date')
    search_fields = ('title', 'description')
    date_hierarchy = 'start_date'
    ordering = ('-start_date',)

admin.site.register(Classroom, ClassroomAdmin)
