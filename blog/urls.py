"""
URL configuration for myblog project.

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
from django.urls import include, path
from .views import about_me, blog_list, page_list, page_detail


handler404 = 'tu_app.views.page_not_found'

urlpatterns = [
    path('about/', about_me, name='about_me'),
    path('pages/', blog_list, name='blog_list'),
    path('admin/', admin.site.urls),
    path('blog/', include('tu_app.urls')),
    path('pages/', page_list, name='page_list'),
    path('pages/<int:page_id>/', page_detail, name='page_detail'),
    path('blog/', include('tu_app.urls')),
]



