from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='index'),
    path('product<int:id>/', views.detail, name='detail'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('editProduct<int:id>/', views.editProduct, name='editProduct'),
    path('deleteProduct<int:id>/', views.deleteProduct, name='deleteProduct'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', views.CustomLogoutView.as_view(template_name='myapp/logout.html'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
