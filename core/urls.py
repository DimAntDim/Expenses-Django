from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('expenses.urls')),
    path('profile/', include('profiles.urls')),
]
