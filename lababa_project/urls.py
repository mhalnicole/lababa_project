from django.contrib import admin
from django.urls import path, include
from operations import views as operations_views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', operations_views.index, name='index'),
    path('operations/', include('operations.urls')),
    path('login/', include('accounts.urls')),
    path('logoff/', accounts_views.logout_view, name='logoff'),
    path('edit-profile/', accounts_views.edit_profile, name='edit_profile'),
]