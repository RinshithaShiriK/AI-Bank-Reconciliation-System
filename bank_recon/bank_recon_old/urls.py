from django.contrib import admin
from django.urls import path
from reconciliation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.upload_file, name='upload'),
    path('dashboard/', views.dashboard, name='dashboard'),
]