from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    name = None
    min_price = None
    max_price = None
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'name':
        name = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        min_price = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        max_price = Phone.objects.all().order_by('-price')
    context = {
        'phones': phones,
        'name': name,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
