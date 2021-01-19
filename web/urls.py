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
    path('manage-profile', views.manage_profile, name='manage-profile'),
    path('index-2', views.index_2, name='index-2'),
    path('movie-category', views.movie_category, name='movie-category'),
    path('movie-details', views.M_details, name='M_details'),
    path('pricing-plan', views.pricing, name='pricing-plan'),
    path('setting', views.setting, name='setting'),
    path('show-category', views.show_category, name='show-category'),
    path('show-details', views.S_details, name='S_details'),
    path('show-signle', views.signle, name='signle'),
    path('show-single', views.single, name='single'),
    path('watch-video', views.watch, name='watch'),
    path('logout/', views.logout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('contact/', views.contact, name='contact'),







]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)