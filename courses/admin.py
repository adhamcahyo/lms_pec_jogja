from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'instructor', 'created_at')
    search_fields = ('name', 'instructor__username')
    list_filter = ('instructor', 'created_at')
    ordering = ('-created_at',)

admin.site.register(Course, CourseAdmin)
