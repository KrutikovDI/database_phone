from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    # sort = request.GET.get['sort']
    # if sort == 'name':
    #     name = Phone.object.filter(name='name')
    # elif sort == 'min_price':
    #     min_price = Phone.object.filter()
    # elif sort == 'max_price':
    #     max_price = Phone.object.filter()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
