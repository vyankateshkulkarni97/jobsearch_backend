from django.urls import path
from .views import register, login_view, logout_view, check_auth

urlpatterns = [
    path('register/', register),
    path('login/', login_view),
    path('logout/', logout_view),
    path('check-auth/', check_auth),
]
