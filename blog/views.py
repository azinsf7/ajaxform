from django.shortcuts import render
from django.http import JsonResponse
from .models import Post

def create_post(request):
    posts = Post.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post': # If you have more than one form in your page you can separate them by using action, so your view will not get multiple requests at the same time.
        title = request.POST.get('title')  # title ro bgir
        description = request.POST.get('description') # description ro bgir

        response_data['title'] = title   #briz to dic khalimon
        response_data['description'] = description

        Post.objects.create(  #To create and save an object in a single step, we are using the create() method.
            title = title,
            description = description,
            )
        return JsonResponse(response_data)

    return render(request, 'create_post.html', {'posts':posts})
