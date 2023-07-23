from django.shortcuts import render, get_object_or_404, redirect
from .models import Discussion
from .forms import DiscussionForm

def discussion_list(request):
    discussions = Discussion.objects.all()
    return render(request, 'discussions/templates/discussions/discussion_list.html', {'discussions': discussions})

def discussion_detail(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id)
    return render(request, 'discussions/templates/discussions/discussion_detail.html', {'discussion': discussion})

def create_discussion(request):
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.user = request.user
            discussion.save()
            return redirect('discussion_list')
    else:
        form = DiscussionForm()
    return render(request, 'discussions/templates/discussions/create_discussion.html', {'form': form})
