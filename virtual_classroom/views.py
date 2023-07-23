from django.shortcuts import render, get_object_or_404, redirect
from .models import Classroom
from .forms import ClassroomForm

def class_list(request):
    classrooms = Classroom.objects.all()
    return render(request, 'virtual_classroom/class_list.html', {'classrooms': classrooms})

def class_detail(request, class_id):
    classroom = get_object_or_404(Classroom, id=class_id)
    return render(request, 'virtual_classroom/templates/virtual_classroom/class_detail.html', {'classroom': classroom})

def create_class(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            classroom = form.save(commit=False)
            classroom.instructor = request.user
            classroom.save()
            return redirect('class_list')
    else:
        form = ClassroomForm()
    return render(request, 'virtual_classroom/templates/virtual_classroom/create_class.html', {'form': form})
