from django.urls import path, include
from blog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('posts/', views.allpost, name='allpost'),
   path('detail/<int:post_id>/', views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)