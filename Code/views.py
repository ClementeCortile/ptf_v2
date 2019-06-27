from django.shortcuts import render, get_object_or_404

from .models import Code


def allCode(request):
    code = Code.objects
    return render(request, 'Code/allcode.html', {'code': code})


def detailcode(request, code_id):
    codedetail = get_object_or_404(Code, pk=code_id)
    return render(request, 'Code/codedetail.html', {'codedetail': codedetail})


def musicchallange(request):
    return render(request, 'Code/Notebooks/MusicChallange.html')


