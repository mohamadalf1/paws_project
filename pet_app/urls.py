from django.urls import path, include
from . import views
from django.contrib import admin
urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.pets, name='pets'),
    path('add-pet/', views.add_pet_form, name='add-pet'),
    path('create-blog/', views.create_blog, name='create-blog'),
    path('blog/', views.blog, name='get_blog'),
    path('admin', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

