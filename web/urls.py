from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index' ),
    path('show-category/', views.show, name='show' ),
    path('movie-category/', views.movie, name='movie' ),
    path('manage-profile/', views.manage, name='manage' ),
    path('movie-details/', views.manage, name='details' ),
    path('pricing-plan/', views.manage, name='pricing' ),
    path('reset-password/', views.manage, name='reset' ),
    path('setting/', views.manage, name='setting' ),
    path('login/', views.manage, name='login' ),
    path('show-details/', views.manage, name='s-details' ),
    path('show-signle/', views.manage, name='signle' ),
    path('show-single/', views.manage, name='single' ),
    path('sign-up/', views.manage, name='sign-up' ),
    path('watch-video/', views.manage, name='watch' ),
    path('index-2/', views.manage, name='index-2' )











]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)