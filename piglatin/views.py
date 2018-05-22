from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request,'home.html')

def translate(request): 
    original = request.GET['originaltext']

    translation= ''
    for word in original.split():
        if word[0] in ['a','e','i','o','u']:
            translation = translation + word
            translation += 'yay '
        else:
            translation +=word[1:]
            translation +=word[0]
            translation +='ay '

    return render(request,'translate.html',{'ORIGINAL': original, 'TRANSLATE':translation})
#python manage.py runserver
