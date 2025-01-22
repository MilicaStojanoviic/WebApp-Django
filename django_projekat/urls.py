"""
URL configuration for django_projekat project.

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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from quotes.views import Register
from django.contrib.auth.views import LogoutView


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('register/success/', TemplateView.as_view(template_name="registration/success.html"), name='register-success'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    #url(r'^quote', include('quotes.urls')),
    path('quote/', include('quotes.urls')),
    path('', include('django.contrib.auth.urls')),
    #url(r'^', include('pages.urls')),
    path('', include('pages.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)