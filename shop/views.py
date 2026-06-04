from django.shortcuts import render, redirect
from django.views import View
from .forms import ShopForm
from .models import LaundryShop


class ShopIndex(View):
    template_name = 'shop/index.html'

    def get(self, request):
        if not request.session.get('username'):
            return redirect('login')
        shops = LaundryShop.objects.all()
        return render(request, self.template_name, {'shops': shops})


class AddShop(View):
    template_name = 'shop/addNewLaundryShop.html'

    def get(self, request):
        if not request.session.get('username'):
            return redirect('login')
        form = ShopForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/shop/')
        else:
            print(form.errors)
        return render(request, self.template_name, {'form': form})


class EditShop(View):
    template_name = 'shop/editLaundryShop.html'

    def get(self, request, shop_id):
        if not request.session.get('username'):
            return redirect('login')
        shop = LaundryShop.objects.get(shop_id=shop_id)
        form = ShopForm(instance=shop)
        return render(request, self.template_name, {'form': form, 'shop': shop})

    def post(self, request, shop_id):
        shop = LaundryShop.objects.get(shop_id=shop_id)
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('/shop/')
        else:
            print(form.errors)
        return render(request, self.template_name, {'form': form, 'shop': shop})


class DeleteShop(View):
    template_name = 'shop/deleteLaundryShop.html'

    def get(self, request, shop_id):
        if not request.session.get('username'):
            return redirect('login')
        shop = LaundryShop.objects.get(shop_id=shop_id)
        return render(request, self.template_name, {'shop': shop})

    def post(self, request, shop_id):
        shop = LaundryShop.objects.get(shop_id=shop_id)
        shop.delete()
        return redirect('/shop/')