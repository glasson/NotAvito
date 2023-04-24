from django.shortcuts import render

def test(request):
    return render(request, template_name="main/footer.html")

def create_post(req):
    return render(req, template_name='main/create_post.html')
