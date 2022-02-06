from django.urls import path
from post.views import *

urlpatterns = [
	path('create', create),
	path('get_list', get_list),
	path('get_post', get_post),
]
