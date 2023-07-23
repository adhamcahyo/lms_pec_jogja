from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Course
from .forms import CourseForm

def edit_course(request, course_id):
    
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', course_id=course.id)
    else:
       
        form = CourseForm(instance=course)

    return render(request, 'courses/edit_course.html', {'form': form, 'course': course})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            messages.success(request, 'Course created successfully.')
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})

def delete_course(request, course_id):
    
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        
        course.delete()
        messages.success(request, 'Course deleted successfully.')
        return redirect('course_list')

    return render(request, 'courses/delete_course.html', {'course': course})
