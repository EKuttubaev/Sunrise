from django.contrib.admin import site

from sunrise.models import Categories, Products

site.register(Categories)
site.register(Products)

