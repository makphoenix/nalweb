from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def intro(request):
    return render(request, 'lessons/intro.html')


@login_required
def chap1_sec1(request):
    return render(request, 'lessons/chap1_sec1.html')


@login_required
def chap1_sec2(request):
    return render(request, 'lessons/chap1_sec2.html')


@login_required
def chap1_sec3(request):
    return render(request, 'lessons/chap1_sec3.html')


@login_required
def chap1_example1(request):
    return render(request, 'lessons/Chapter1-Example1.html')


@login_required
def chap1_example2(request):
    return render(request, 'lessons/Chapter1-Example2.html')


@login_required
def chap1_example3(request):
    return render(request, 'lessons/Chapter1-Example3.html')


@login_required
def chap1_example4(request):
    return render(request, 'lessons/Chapter1-Example4.html')


@login_required
def chap1_example5(request):
    return render(request, 'lessons/Chapter1-Example5.html')


@login_required
def chap1_example6(request):
    return render(request, 'lessons/Chapter1-Example6.html')


@login_required
def chap1_example7(request):
    return render(request, 'lessons/Chapter1-Example7.html')


@login_required
def chap1_example8(request):
    return render(request, 'lessons/Chapter1-Example8.html')


@login_required
def chap2_sec1(request):
    return render(request, 'lessons/chap2_sec1.html')


@login_required
def chap2_sec2(request):
    return render(request, 'lessons/chap2_sec2.html')


@login_required
def chap2_sec3(request):
    return render(request, 'lessons/chap2_sec3.html')


@login_required
def chap2_sec4(request):
    return render(request, 'lessons/chap2_sec4.html')


@login_required
def chap2_sec5(request):
    return render(request, 'lessons/chap2_sec5.html')


@login_required
def chap2_sec6(request):
    return render(request, 'lessons/chap2_sec6.html')


@login_required
def chap2_sec7(request):
    return render(request, 'lessons/chap2_sec7.html')


@login_required
def chap2_example1(request):
    return render(request, 'lessons/Chapter2-Example1.html')


@login_required
def chap2_example2(request):
    return render(request, 'lessons/Chapter2-Example2.html')


@login_required
def chap2_example3(request):
    return render(request, 'lessons/Chapter2-Example3.html')


@login_required
def chap2_example4(request):
    return render(request, 'lessons/Chapter2-Example4.html')


@login_required
def chap2_example5(request):
    return render(request, 'lessons/Chapter2-Example5.html')


@login_required
def chap2_example6(request):
    return render(request, 'lessons/Chapter2-Example6.html')


@login_required
def chap2_example7(request):
    return render(request, 'lessons/Chapter2-Example7.html')


@login_required
def chap2_example8(request):
    return render(request, 'lessons/Chapter2-Example8.html')


@login_required
def chap2_example9(request):
    return render(request, 'lessons/Chapter2-Example9.html')


@login_required
def chap3_sec1(request):
    return render(request, 'lessons/chap3_sec1.html')


@login_required
def chap3_sec2(request):
    return render(request, 'lessons/chap3_sec2.html')


@login_required
def chap3_example1(request):
    return render(request, 'lessons/Chapter3-Example1.html')


@login_required
def chap3_example2(request):
    return render(request, 'lessons/Chapter3-Example2.html')


@login_required
def chap3_example3(request):
    return render(request, 'lessons/Chapter3-Example3.html')


@login_required
def chap3_example4(request):
    return render(request, 'lessons/Chapter3-Example4.html')
