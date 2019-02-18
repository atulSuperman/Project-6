"""indiahealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from signup import views as v1
from home import views as v2
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$',v1.signin, name = 'signin'),
    url(r'^postsignin/', v1.postsignin, name = "postsignin"),
    url(r'^$',v1.logout,name="log"),
    url(r'^home/',v2.home,name = "home"),
    url(r'^signup/',v1.signUp,name='signup'),
    url(r'^postsignup/',v1.postsignup,name='postsignup'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# sudo fuser -k 8000/tcp