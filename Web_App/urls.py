"""Web_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home$', views.home, name='home'),
    url(r'^login$', views.login, name='login'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^properties$', views.properties, name='properties'),
    url(r'^about$', views.about, name='about'),
    url(r'^blog-home$', views.bloghome, name='blog-home'),
    url(r'^single-blog$', views.singleblog, name='single-blog'),
    url(r'^agents$', views.agents, name='agents'),
    url(r'^elements$', views.elements, name='elements'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^searchresult$', views.searchresult, name='searchresult'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()