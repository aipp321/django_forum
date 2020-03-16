from django.shortcuts import render,redirect
from datetime import datetime
from .models import Article, Text_type
from login.models import User
from time import sleep
# Create your views here.


def forum_show(request):
    if not request.session.get('is_login',None):
        return redirect('/login/')
    if request.method == 'GET':
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        Text_all = Article.objects.all()
        Text_type_all = Text_type.objects.all()
        context = {}
        context['now'] = now
        context['text'] = Text_all
        context['text_type'] = Text_type_all
        return render(request, 'forum/forum.html', context)
    elif request.method == 'POST':
        new_Article = Article()
        Text_type_all = Text_type.objects.all()
        rec_text_type = request.POST.get('text_type')
        new_text_type = Text_type()
        if rec_text_type not in Text_type.objects.all():
            new_text_type.type_name = rec_text_type
            new_text_type.save()
        new_Article.title = request.POST.get('title')
        new_Article.content = request.POST.get('context')

        new_Article.author= User.objects.get(name=request.session['user_name'])
        new_Article.type = Text_type.objects.get(type_name=rec_text_type)
        new_Article.save()

        return redirect('/forum/')
    else:
        return render(request, 'forum/forum.html', locals())