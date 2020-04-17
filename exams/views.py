from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def exam1(request):
    return render(request, 'exams/exam1.html')
