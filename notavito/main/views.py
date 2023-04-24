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

#made by yaroslav
def home(request):
    post = Post.objects.all()
    post = post.filter().order_by("-id")[:8]
    pposts = []
    for posts in post:
        print(posts)
        pposts.append(posts)
    return render(request, 'main/home.html', context={
        'title1':pposts[0].title,
        'title2':pposts[1].title,
        'title3':pposts[2].title,
        'title4':pposts[3].title,
        'title5':pposts[4].title,
        'title6':pposts[5].title,
        'title7':pposts[6].title,
        'title8':pposts[7].title,
        'id1':pposts[0].id,
        'id2':pposts[1].id,
        'id3':pposts[2].id,
        'id4':pposts[3].id,
        'id5':pposts[4].id,
        'id6':pposts[5].id,
        'id7':pposts[6].id,
        'id8':pposts[7].id,
        })
