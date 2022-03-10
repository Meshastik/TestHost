from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import View
from django.views.generic import ListView
from .forms import *


class PostViewList(ListView):
    model = Post
    template_name = 'app/main.html'
    context_object_name = 'list_post'


class CreatePostView(View):
    def post(self, request):
        post_form = PostForms(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('list_post')

    def get(self, request):
        get_form = PostForms()
        return render(request, 'app/create_post.html', {'form': get_form})



