from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.


def setcookie(request):
    response = render(request, 'student/setcookie.html', )
    response.set_cookie('name', 'Sonam',
                        expires=datetime.utcnow()+timedelta(days=2))
    return response


def getcookie(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get('Name')
    print(name)
    return render(request, 'student/getcookie.html', context={'name': name})


def delcookie(request):
    response = render(request, 'student/delcookie.html')
    response.delete_cookie('name')
    return response
