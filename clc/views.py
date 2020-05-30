from django.http import HttpResponse
from django.shortcuts import render

def add(request):
    return render(request,'clc.html')

def evl(request):
    ans = request.GET.get('answer')
    a = eval(ans)
    print(a)
    ans1 = {'pop':a}
    return render(request,'clc.html',ans1)