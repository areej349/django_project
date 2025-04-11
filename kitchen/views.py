from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import KitchenProduct  # تأكد من استخدام الموديل الخاص بأدوات المطبخ

# دالة لعرض المنتجات الخاصة بأدوات المطبخ
def list_kitchen(request):
    # استعراض المنتجات الخاصة بأدوات المطبخ من قاعدة البيانات
    kitchen_products = KitchenProduct.objects.all()
    context = {'kitchen_products': kitchen_products}
    return render(request, 'list_kitchen.html', context)

# دالة لعرض تفاصيل المنتج
def show_kitchen(request, item_id):
    product = KitchenProduct.objects.get(id=item_id)  # جلب المنتج بناءً على الـ ID
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)  # عرض تفاصيل المنتج

# دالة لعرض الفئات
@csrf_exempt
def categories(request):
    template = loader.get_template('categories.html')
    x = request.POST.get('title')
    y = request.POST.get('address')
    value = {
        'title': x,
        'address': y
    }
    return HttpResponse(template.render(value))

# دالة لقراءة البيانات من قاعدة البيانات
def products(request):
    prd = KitchenProduct.objects.all()  # جلب كل المنتجات من قاعدة البيانات الخاصة بأدوات المطبخ
    print(prd) 
    return HttpResponse(prd)

# طريقة أخرى لعرض البيانات عبر قالب
def products(request):
    template = loader.get_template('products.html')
    prd = KitchenProduct.objects.all()
    value = {
        'prod': prd
    }
    return HttpResponse(template.render(value))
