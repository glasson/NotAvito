from django.shortcuts import render, redirect
from .forms import PostForm
from django.http import HttpResponse

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