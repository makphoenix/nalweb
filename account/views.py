from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        user_password = request.POST['password']

        user = auth.authenticate(username=user_name, password=user_password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')
    else:
        return render(request, 'account/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')


def password(request):
    return render(request, 'account/password.html')


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['FirstName']
        last_name = request.POST['LastName']
        email = request.POST['email']
        username = request.POST['username']
        first_password = request.POST['password']
        confirm_password = request.POST['ConfirmPassword']

        # Check for password match
        if first_password == confirm_password:
            # Check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That USERNAME is taken!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That EMAIL is being used!')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, email=email, password=first_password,
                                                    first_name=first_name, last_name=last_name)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('dashboard')
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do NOT match!')
            return redirect('register')
    else:
        return render(request, 'account/register.html')


@login_required
def dashboard(request):

    # messages.success(request, 'You are now logged in')
    return render(request, 'base_dashboard.html')
