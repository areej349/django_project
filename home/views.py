from django.shortcuts import render,redirect
from django.http import HttpResponse ,JsonResponse
from django.template import loader
from .models import Product,Categories,Order
from django.contrib.auth.decorators import login_required  #مكتبة تجعني اطبق شرط قبل اي دالة وجوب تسجيل الدخول
from django.views.decorators.csrf import csrf_exempt
import requests
# Create your views here.


def showland(request):
    if 'cart_count' not in request.session:  #اذا استخدمت متصفح اخر ما يعرف الكارت كاونت ف اسوي دالة تنشئة وتعطيه قيمة صفر
           request.session['cart_count']=0

    template=loader.get_template('landpage.html')
    categories=Categories.objects.all()
    data={
        'categories':categories,
        'cart_count':request.session['cart_count']
    }
    return HttpResponse(template.render(data,request))


# مهمتها تقرا  - تظهر المنتجات حسب الفئة
def list_product(request,id):
        if 'cart_count' not in request.session:  #اذا استخدمت متصفح اخر ما يعرف الكارت كاونت ف اسوي دالة تنشئة وتعطيه قيمة صفر
           request.session['cart_count']=0

        template=loader.get_template('list_products.html')
        products=Product.objects.filter(categories_id=id)
        data={
              'product':products,
              'cart_count':request.session['cart_count']

        }

        return HttpResponse(template.render(data,request))


#دالة تشغل صفحة الproductdetail
def product_details(request,id):
        if 'cart_count' not in request.session:  #اذا استخدمت متصفح اخر ما يعرف الكارت كاونت ف اسوي دالة تنشئة وتعطيه قيمة صفر
           request.session['cart_count']=0
        products=Product.objects.select_related('categories').get(id=id)  #نستخدم get عشان يرجع سجل واحد اما فلتر يرجع اوبجكت ولازم نستخدم فور ايتش

        data={
              'cart_count':request.session['cart_count'],
              'products':products

        }
        template=loader.get_template('productdetails.html')
        return HttpResponse(template.render(data,request))

#دالة وظيفتها لما المستخدم يضيف للسلة العداد يحتفظ بها داخل session
def add_to_cart(request):
       request.session['cart_count']=request.session.get('cart_count',0)+1   #روح جيب القيمة الاولى او المتغير السابق او قيمة السلة او القيمة القديمة اذا مافيه قيمه مثل لو المستخدم يدخل لاول مره يعطيه صفر واذا موجودة ضيف عليها واحد
       request.session.modfied=True  #عدل الاضافة
       return JsonResponse({'cart_count':request.session['cart_count']}) #راح ترجع قيمة العداد بصيغة json جافا سكربت



@csrf_exempt
@login_required
def checkout(request):
       if 'cart_count' not in request.session:  #اذا استخدمت متصفح اخر ما يعرف الكارت كاونت ف اسوي دالة تنشئة وتعطيه قيمة صفر
           request.session['cart_count']=0
       data={
              'cart_count':request.session['cart_count'],

        }
       template=loader.get_template('checkout.html')
       return HttpResponse(template.render(data,request))



def get_api(request):
    api_url='https://fakestoreapi.com/products'
       
    response=requests.get(api_url)
    if response.status_code==200:
        data=response.json()
    else:
        data={"error":f"error:{response.status_code}"}
       
    template=loader.get_template('get_api.html')
    return render(request,'get_api.html',{'api_data':data})


#invoice
def process_payment(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        cardnumber = request.POST.get('cardnumber')
        cvv = request.POST.get('cvv')
        exp_month = request.POST.get('exp_month')
        exp_year = request.POST.get('exp_year')

        # تقدر هنا تسوي:
        # - حفظ الفاتورة في قاعدة البيانات
        # - إرسال بريد إلكتروني
        # - أو فقط طباعة على الشاشة مثلاً

        context = {
            'fullname': fullname,
            'email': email,
            'cardnumber': cardnumber,
            'cvv': cvv,
            'exp_month': exp_month,
            'exp_year': exp_year,
        }

        return render(request, 'invoice.html', context)

    return redirect('checkout')  # لو دخل على الصفحة بغير POST



#search
def search(request):
    if 'cart_count' not in request.session:
        request.session['cart_count'] = 0
    
    query = request.GET.get('query', '')  # جلب النص المدخل من المستخدم في خانة البحث
    
    # إذا كانت هناك قيمة للبحث، نبحث في المنتجات بناءً على النص المدخل في `name` و `categories`
    if query:
        products = Product.objects.filter(name__icontains=query) | Product.objects.filter(categories__name__icontains=query)
    else:
        products = Product.objects.all()  # إذا لم يتم إدخال أي قيمة، نعرض جميع المنتجات
    
    data = {
        'products': products,
        'cart_count': request.session['cart_count'],
    }

    return render(request, 'search.html', data)

