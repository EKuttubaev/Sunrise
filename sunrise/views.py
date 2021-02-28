from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from sunrise.forms import ProductForm, CategoryForm
from sunrise.models import Products


class IndexView(TemplateView):
    template_name = "index.html"


class AddCategoryView(TemplateView):
    template_name = "add_category.html"

    def dispatch(self, request, *args, **kwargs):
        form = CategoryForm()
        if request.method == "POST":
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/")
        return render(request, self.template_name, {"form": form})


class AddProductsView(TemplateView):
    template_name = "products_page.html"

    def dispatch(self, request, *args, **kwargs):
        form = ProductForm()
        if request.method == "POST":
            form = ProductForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect("/")
        return render(request, self.template_name, {"form": form})


class ProductsView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        products = Products.objects.all()
        return render(request, "products_list.html", context={
            "products": products
        })

    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Товар"
