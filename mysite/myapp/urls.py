from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('product<int:id>/', views.detail, name='detail'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('editProduct<int:id>/', views.editProduct, name='editProduct'),
    path('deleteProduct<int:id>/', views.deleteProduct, name='deleteProduct'),
    path('dashboard/', views.dashboard, name='dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
