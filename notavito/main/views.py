from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return HttpResponseRedirect('main')
    else:
        form = PostForm()
    return render(request, 'main/create_post.html', {'form': form, 'user': request.user})

def search(request):
    search_word = request.GET.get('search')
    try:
        if len(founded_posts := Post.objects.filter(title__icontains=search_word)) != 0:
            return render(request, 'main/search_page.html', context={'posts': founded_posts})
        else:
            return render(request, 'main/not_founded.html')
    except:
        return render(request, 'main/not_founded.html')

def delete_post(request, post_id):
    post_object = get_object_or_404(Post, id=post_id) #если не нашел отправить 404
    if request.method == "POST":
        post_object.delete()
        return render(request, template_name='main/success_deleted.html')


def edit_post(request, post_id):
    record = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = PostForm(instance=record)

    return render(request, 'edit_post.html', {'form': form, 'record': record})

def main():
    return HttpResponse("main")