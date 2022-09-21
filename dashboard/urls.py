from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('register',views.register, name='register'),
    path('logout',views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('blog-topic', views.blogTopic, name='blogTopic'),
    path('blog-section', views.blogSection, name='blog-section')




    # path('dashboard', views.dashboard, name="dashboard")

]
