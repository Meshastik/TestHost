from django.urls import path
from .views import CreatePostView, PostViewList


urlpatterns = [
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('main/', PostViewList.as_view(), name='list_post')
]
