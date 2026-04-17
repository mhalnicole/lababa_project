from django.shortcuts import render
from django.views import View
from .forms import ShopForm


class ShopIndex(View):
    template_name = 'shop/index.html'

    def get(self, request):
        return render(request, self.template_name)


class AddShop(View):
    template_name = 'shop/addNewLaundryShop.html'

    def get(self, request):
        form = ShopForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return render(request, self.template_name, {'form': form})