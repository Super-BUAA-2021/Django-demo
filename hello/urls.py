from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
	path('user/', include(('user.urls', 'user'), namespace="user")),
	path('post/', include(('post.urls', 'post'), namespace="post")),
]
