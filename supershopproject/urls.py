"""supershopproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, re_path
from django.http import HttpResponse
from shop import views
from django.views.generic import RedirectView

from shop.views import VueAppView

from django.views.generic import TemplateView

# from shop.views import IndexTemplateView

urlpatterns = [
    # re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
    path('vueapp/', VueAppView.as_view()),
    path('build/', views.build),
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('adminka/orders/', views.adminOrders),
    path('adminka/products/add/', views.adminProductsAdd),
    path('adminka/products/delete/', views.adminProductsDelete),
    path('product/<int:productID>/', views.productByProductID),
    path('users/bucket/delete/', views.usersBucketDelete),
    path('users/bucket/buy/', views.usersBucketBuy),
    path('users/amount/', views.usersAmount),
    path('users/check/', views.usersCheck),
    path('users/usercreatesuccess/', views.usersUsercreatesuccess),
    path('users/bucket/add/', views.usersBucketAdd),
    path('users/bucket/', views.usersBucket),
    path('<str:route>/', views.otherRoutes),
    path('<str:route>/<str:secondroute>', views.otherRoutes),
    path('<str:route>/<int:secondroute>', views.otherRoutes),
    path('', TemplateView.as_view(template_name='index.html'), name='index')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
