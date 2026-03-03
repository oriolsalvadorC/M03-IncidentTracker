"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from core.views import perfil_usuari, vulnerable_search
from core.views import perfil_usuari, vulnerable_search, update_email, incident_detail


urlpatterns = [
    path('admin/', admin.site.urls),

    # activa /accounts/login/ i /accounts/logout/
    path('accounts/', include('django.contrib.auth.urls')),
    path('perfil/', perfil_usuari, name='perfil'),
    path('search/', vulnerable_search, name='vulnerable_search'),
    path('update-email/', update_email, name='update_email'),
    path('incident/<int:id>/', incident_detail, name='incident_detail')

]

