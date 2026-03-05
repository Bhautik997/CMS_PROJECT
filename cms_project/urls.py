from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/login/', auth_views.LoginView.as_view(template_name='login.html', next_page='/admin/'), name='admin_login'),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', include('cms.urls')),
]

admin.site.login_template = 'login.html'