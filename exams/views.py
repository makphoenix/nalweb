from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
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

        # Question 2
        input2_1 = float(request.POST['input2_1'])
        input2_2 = float(request.POST['input2_2'])
        input2_3 = float(request.POST['input2_3'])

        if input2_1 == 1:
            exam01_mark += 1

        if abs(input2_2 - 1) <= 0.5:
            exam01_mark += 0.5

        if abs(input2_3 - 2) <= 0.5:
            exam01_mark += 0.5

        # Question 3
        input3_1 = float(request.POST['input3_1'])

        if abs(input3_1 - 2.1284) <= 0.001:
            exam01_mark += 2

        # Question 4
        input4_1 = float(request.POST['input4_1'])

        if abs(input4_1 - 1.0886) <= 0.001:
            exam01_mark += 2

        # Question 5
        input5_1 = float(request.POST['input5_1'])

        if abs(input5_1 - 0.5928) <= 0.001:
            exam01_mark += 2

        # Question 6
        input6_1 = float(request.POST['input6_1'])
        input6_2 = float(request.POST['input6_2'])
        input6_3 = float(request.POST['input6_3'])

        if abs(input6_1 - 0.571) <= 0.001:
            exam01_mark += 0.75

        if abs(input6_2 - 2.8571) <= 0.001:
            exam01_mark += 0.75

        if abs(input6_3 - 3) <= 0.1:
            exam01_mark += 0.5

        # Question 7
        input7_1 = float(request.POST['input7_1'])

        if abs(input7_1 - 3.3511) <= 0.001:
            exam01_mark += 2

        # Question 8
        input8_1 = float(request.POST['input8_1'])
        input8_2 = float(request.POST['input8_2'])
        if abs(input8_1 - 0.04) <= 0.01:
            exam01_mark += 1

        if abs(input8_2 - 0.828) <= 0.001:
            exam01_mark += 1

        # Question 9
        input9_1 = float(request.POST['input9_1'])

        if abs(input9_1 - 1.003) <= 0.001:
            exam01_mark += 2

        # Question 10
        input10_1 = float(request.POST['input10_1'])
        input10_2 = float(request.POST['input10_2'])
        input10_3 = float(request.POST['input10_3'])

        if abs(input10_1 - 1) <= 0.1:
            exam01_mark += 0.75

        if abs(input10_2 - (-1)) <= 0.1:
            exam01_mark += 0.75

        if abs(input10_3 - 2) <= 0.1:
            exam01_mark += 0.5

        messages.warning(request, 'نمره نهایی: ' + str(exam01_mark))
        return render(request, 'exams/exam01_cast.html')
        # return redirect('exam01')
    else:
        return render(request, 'exams/exam01_cast.html')


@login_required
def exam02(request):
    if request.method == 'POST':
        exam02_mark = 0

        # Question 1
        input1_1 = float(request.POST['input1_1'])

        if abs(input1_1 - 0.434) <= 0.001:
            exam02_mark += 2

        # Question 2
        input2_1 = float(request.POST['input2_1'])

        if input2_1 == 2:
            exam02_mark += 0.75

        return render(request, 'exams/exam02_cast.html')
    else:
        return render(request, 'exams/exam02_cast.html')


@login_required
def exam03(request):
    if request.method == 'POST':
        exam03_mark = 0

        return render(request, 'exams/exam03_cast.html')
    else:
        return render(request, 'exams/exam03_cast.html')


@login_required
def exam04(request):
    if request.method == 'POST':
        exam04_mark = 0

        return render(request, 'exams/exam04_cast.html')
    else:
        return render(request, 'exams/exam04_cast.html')


@login_required
def exam05(request):
    if request.method == 'POST':
        exam05_mark = 0

        return render(request, 'exams/exam05_cast.html')
    else:
        return render(request, 'exams/exam05_cast.html')
