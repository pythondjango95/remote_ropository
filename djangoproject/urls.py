from django.contrib import admin
from django.urls import path,include
from djangoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('djangoapp.urls'))
]
