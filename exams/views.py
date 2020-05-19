from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def exam01(request):
    return render(request, 'exams/exam01_cast.html')
