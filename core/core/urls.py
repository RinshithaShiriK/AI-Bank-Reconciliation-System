from django.contrib import admin
from django.urls import path
from core.reconciliation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.upload_file),        # Home page
    path('dashboard/', views.dashboard),
]