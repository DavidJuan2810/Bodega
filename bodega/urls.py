"""
URL configuration for bodega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#incluir la clase que se acaba de crear en apps/post/api/views
from apps.registro.api.views import RegistroApiView
from apps.salida.api.views import SalidaApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/reg/', RegistroApiView.as_view()),
    path('api/sal/', SalidaApiView.as_view())
]
