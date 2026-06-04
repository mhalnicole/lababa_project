from django.urls import path
from .views import login_page, logout_user, edit_profile

urlpatterns = [
    path('', login_page, name='login'),
    path('logout/', logout_user, name='logout_user'),
    path('edit-profile/', edit_profile, name='edit_profile'),
]