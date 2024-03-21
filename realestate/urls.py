from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='realestate_home'),
    # path('details/<int:pk>/<slug:slug>/', views.Detail.as_view(), name='realestate_detail'), فارسی رو برای یو آر ال ارسال کردن پشتیبانی نمیکرد. مجبور میشیم از رگولار اکسپرشن استفاده کنیم که از تو مونگارد دیدم ۶ دقه رو.
    re_path(r'details/(?P<pk>[-\w]+)/(?P<slug>[-\w]+)/', views.Detail.as_view(), name='realestate_detail'),
]
