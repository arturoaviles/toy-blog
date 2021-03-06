from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from blog import views

router = routers.DefaultRouter()
router.register(r'writers', views.WriterViewSet)
router.register(r'articles', views.ArticleViewSet)


urlpatterns = [
    path('', include('blog.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
