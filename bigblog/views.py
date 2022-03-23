from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail

from .forms import LoginForm, UserRegistrationForm, EmailPostForm
from .models import Post, Comment



# Create your views here.

# class PostListView(ListView): 
#     queryset = Post.objects.all()
#     context_object_name  = "posts"
#     paginate_by = 3
#     template_name = "bigblog/post/list.html"


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


def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 3)      # 3 posts in each num_pages 

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #if page is not a integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        #if page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, "bigblog/post/list.html", {"page": page, 'posts': posts})



def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request, "bigblog/post/detail.html", {'post':post})


def post_share(request, post_id):
    #Retreive post by id
    post = get_object_or_404(Post, id = post_id, status = "published")
    send = False
    if request.method == "POST":
        #Form was submitted 
        form = EmailPostForm(request.POST)
        if form.is_valid():
            #Form fields passed validation
            cd = form.cleaned_data
            post_url= request.build_absolute_url(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, "yrysbek.or.s@gmail.com", [cd['to']])
            send = True
           # ... send email

    else: 
        form = EmailPostForm()

    return render(request, "bigblog/post/share.html", {
                            "post": post, 
                            "form": form,
                            'sent': sent})