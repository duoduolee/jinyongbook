from django.shortcuts import render
# Create your views here.
from .models import Novel

def chapter_list(request):
    Novels = Novel.objects.all()
    return render(request, 'chapter_list.html', {'Novels': Novels})


def chapter(request,novel_id):
    content = Novel.objects.get(id='%s'% novel_id)
    return render(request, 'chapter.html', {'content': content})