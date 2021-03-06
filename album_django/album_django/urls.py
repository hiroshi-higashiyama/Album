from os import name
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from post.views import CustomView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('post.urls')),
    path('', CustomView.as_view(), name='Custom')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
