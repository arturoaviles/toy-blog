from django.urls import path

from .views import articleApprovalView, articlesEditedView, homePageView, \
    articleDetailView, articleCreateView, registerView, loginView, logoutView

urlpatterns = [
    path('', homePageView, name='dashboard'),
    path('register/', registerView, name='register'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),
    path('article/', articleCreateView, name='article-create'),
    path('article/<str:pk>', articleDetailView, name='article-edit'),
    path('article-approval/', articleApprovalView, name='approval'),
    path('articles-edited/', articlesEditedView, name='edited')
]
