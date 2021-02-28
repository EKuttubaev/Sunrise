"""sunrise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from django.urls import path

from sunrise.accounts.accounts import RegisterView, LogoutView, UserChangeView, ProfileView
from sunrise.views import IndexView, AddProductsView, AddCategoryView, ProductsView

urlpatterns = [
                  path('', IndexView.as_view(), name="index"),
                  path('accounts/login/', LoginView.as_view(), name="login"),
                  path('accounts/profile/', ProfileView.as_view(), name="profile"),
                  path('accounts/logout/', LogoutView.as_view(), name="logout"),
                  path('accounts/register/', RegisterView.as_view(), name="register"),
                  path('accounts/change_profile/', UserChangeView.as_view(), name="change_profile"),
                  path('products_list/', ProductsView.as_view(), name="products_list"),
                  path('products_page/', AddProductsView.as_view(), name="add_products"),
                  path('add_category/', AddCategoryView.as_view(), name="add_category"),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
