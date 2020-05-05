from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

# from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, \
#     PasswordResetConfirmView, PasswordResetCompleteView


# urlpatterns = [
#     path('', views.login, name='login'),
#     path('password', views.password, name='password'),
#     path('dashboard', views.dashboard, name='dashboard'),
#     path('register', views.register, name='register'),
#     path('logout', views.logout, name='logout'),
#     # path('reset-password', PasswordResetView.as_view(), name='password_reset'),
#     path('reset-password', PasswordResetView.as_view(), name='password_reset'),
#     path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
#     # path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/', PasswordResetConfirmView.as_view(),
#     #      name='password_reset_confirm'),
#     path('reset-password/confirm/<uidb64>[0-9]<token>/', PasswordResetConfirmView.as_view(),
#          name='password_reset_confirm'),
#     path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
# ]


urlpatterns = [
    path('', views.login, name='login'),
    # path('', auth_views.LoginView.as_view(), name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
