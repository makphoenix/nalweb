from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def exam01(request):
    if request.method == 'POST':
        exam01_mark = 0

        # Question 1
        input1_1 = float(request.POST['input1_1'])
        input1_2 = float(request.POST['input1_2'])
        if abs(input1_1 - 1.194) <= 0.001:
            exam01_mark += 1

        if abs(input1_2 - 0.0012965) <= 0.0000001:
            exam01_mark += 1
    else:
        return render(request, 'exams/exam01_cast.html')
