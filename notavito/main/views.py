from django.shortcuts import render, redirect
from .forms import PostForm
from django.http import HttpResponse
from .models import Post

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