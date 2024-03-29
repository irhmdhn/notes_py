from django.shortcuts import render, redirect

from .models import Document

def index(request):
    noteid = int(request.GET.get('noteid', 0))
    notes = Document.objects.all()

    if request.method == 'POST':
        noteid = int(request.POST.get('noteid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')

        if noteid > 0:
            note = Document.objects.get(pk=noteid)
            note.title = title
            note.content = content
            note.save()

            return redirect('/?noteid=%i' % noteid)
        else:
            note = Document.objects.create(title=title, content=content)

            return redirect('/?noteid=%i' % note.id)

    if noteid > 0:
        note = Document.objects.get(pk=noteid)
    else:
        note = ''

    context = {
        'noteid': noteid,
        'notes': notes,
        'note': note
    }

    return render(request, 'index.html', context)

def delete_note(request, noteid):
    note = Document.objects.get(pk=noteid)
    note.delete()

    return redirect('/')

