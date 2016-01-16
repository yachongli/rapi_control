from django.shortcuts import render

def index(request):
    return render(request,'index.html',{})

def calendar(request):
    return render(request,'calendar.html',{})

