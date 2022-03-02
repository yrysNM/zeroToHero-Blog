from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login

from .forms import LoginForm, UserRegistrationForm

#ffrom  .models import User 
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'bigblog/login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'bigblog/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'bigblog/register.html', {'user_form': user_form})


# def just(request):
#     object_list = User.objects.all()
#     return render(request, 'bigblog/third_page.html', {'object_list': object_list})

# def thanks_page(request):
#     name = request.POST.get('name',  False)
#     email = request.POST.get('email', False)
#     password = request.POST.get('password', False)
#     element = User(name=name, email=email, password=password)
#     element.save()
#     return render(request, 'bigblog/thanks.html', {'name': name,
#                                              'email': email,
#                                              'password': password})