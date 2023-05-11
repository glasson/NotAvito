from django.shortcuts import render, redirect
from .forms import PostForm
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User

def test(request):
    return render(request, template_name="main/footer.html")

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return HttpResponse("Успешно")
    else:
        form = PostForm()
    return render(request, 'main/header.html', {'form': form})

def search(request):
    search_word = request.GET.get('search')
    try:
        if len(founded_posts := Post.objects.filter(title__icontains=search_word)) != 0:
            return render(request, 'main/search_page.html', context={'posts': founded_posts})
        else:
            return render(request, 'main/not_founded.html')
    except:
        return render(request, 'main/not_founded.html')

def profile(request):
    id = request.GET.get("id", 0)
    user = User.objects.all()
    user = user.filter(
        id = id
    )
    if (user.exists()):
        for profile in user:
            print(f"{profile.id} {profile.username} {profile.first_name} {profile.last_name} {profile.last_login}")
    else:
        id=0
    if id == 0:
        return render(request, 'main/profile.html', context={
            'id': 'None',
            'username':'None',
            'first_name': 'None',
            'last_name': 'None',
            'email': 'None',
            'last_login':'None'    
        })
    else:
        return render(request, 'main/profile.html', context={
            'id':profile.id,
            'username':profile.username,
            'first_name':profile.first_name,
            'last_name':profile.last_name,
            'email':profile.email,
            'last_login':profile.last_login}) 
            
    
    
    # try:
    #     if len(profile := user.objects.filter(id=2)) != 0:
    #             return render(request, 'main/profile.html', context={'posts': user})
    #     else:
    #         return render(request, 'main/not_founded.html')
    # except:
    #     return render(request, 'main/not_founded.html')
    return render(request,'main/profile.html')

    # users = UserModel.objects.filter(
    #     first_name='1',
    # ).order_by(
    #     '-last_name'
    # )
    # for user in users:
    #     print(user.last_name)

