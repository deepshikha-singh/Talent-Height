from django.urls import path
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index' ),
    path('register-into-talentheight', views.signup, name='signup'),
    path('login-into-talentheight', views.signin, name='signin'),
    
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_chang.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('manage-profile', views.manage, name='manage'),
    path('index-2', views.manage, name='index-2'),
    path('movie-category', views.manage, name='M_category'),
    path('movie-details', views.manage, name='M_details'),
    path('pricing-plan', views.manage, name='pricing'),
    path('setting', views.manage, name='setting'),
    path('show-category', views.manage, name='S_category'),
    path('show-details', views.manage, name='S_details'),
    path('show-signle', views.manage, name='signle'),
    path('show-single', views.manage, name='single'),
    path('watch-video', views.manage, name='watch'),
    path('logout/', views.log_out, name='logout'),






]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)