"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf.urls import include, url, patterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', include('qa.views')),
    url(r'^login/.*$', include('qa.views')),
    url(r'^signup/.*$', include('qa.views')),
    url(r'^question/\d+/$', include('qa.views')),
    url(r'^ask/.*$', include('qa.views')),
    url(r'^popular/.*$', include('qa.views')),
    url(r'^new/.*$', include('qa.views'))
]
