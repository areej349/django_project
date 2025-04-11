from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import product
# Create your views here.


def list_electronic(request):
    electronic=[
        {'id':1, 'name':'laptop Dell 15 inspiron', 'price':3700, 'description':'laptop Dell 15 inspiron cor i7 SSD RAM 16GB', 'image':'https://img.freepik.com/free-vector/laptop-realistic_78370-511.jpg?t=st=1743974783~exp=1743978383~hmac=a445d0e0347ef8d5c97e9966c0301148bd99da1a0f7dc892331ebd1a3e49b034&w=826'},
        {'id':2, 'name':'laptop lenovo ', 'price':3800, 'description':'laptop cor i7 SSD RAM 16GB', 'image':'https://img.freepik.com/free-vector/laptop-realistic_78370-511.jpg?t=st=1743974783~exp=1743978383~hmac=a445d0e0347ef8d5c97e9966c0301148bd99da1a0f7dc892331ebd1a3e49b034&w=826'},
        {'id':3, 'name':'iphone 16 pro ', 'price':4800, 'description':'iphone 16 pro  SSD RAM 16GB', 'image':'https://img.freepik.com/free-psd/iphone-15-pro-mockup-front-back-view_1332-60588.jpg?t=st=1743976153~exp=1743979753~hmac=aafe9e35f165d8a71297cf39e1363c6808d219033865c4ea1f2779bfc3d349d2&w=740'},
        {'id':4, 'name':'samsung s 24 ', 'price':3500, 'description':'samsung s 24  SSD RAM 16GB', 'image':'https://img.freepik.com/free-vector/realistic-style-new-smartphone-model_23-2148380821.jpg?t=st=1743976263~exp=1743979863~hmac=6e764fbb462f7f2c8aa5d778737a59ea88e5c0ad364459dc0ab0771ddd8c8231&w=826'},

    ]

    context={
   'electronic':electronic 
}


    template=loader.get_template('list_electronic.html')
    return HttpResponse(template.render(context))



# Create 2 --- phone page
# دالة مهمتها تشغيل صفحة phone  // هذي دالة تستقبل براميتر من phone //
def showphone(request,phone):
    template=loader.get_template('phone.html')
#لازم اخزن البراميتر داخل object 
    value={
        'ph':phone #مفتاح
    }
    print(phone)
    return HttpResponse(template.render(value)) # ثم الobject اللي اسمه فاليو نرسله للصفحة عشان يطبعه

# create 4 --- category page
@csrf_exempt

def categories(request): #معنى الrequest  هو طلبات الhttp  #كل القيم تتخزن في الريكوست 
        template=loader.get_template('categories.html')
        x=request.POST.get('title')   #لان طريقة الطلب في الفورم هي بوست  #جيب لي القيمة المخزنة في التايتل 
        y=request.POST.get('address') #جيب لي القيمة المخزنة في الادريس 

        value={   #انشئ اوبجكت لما ابغى ارسل القيم ل عرضها بالمتصفح
             'title':x,
             'address':y
        }
        return HttpResponse(template.render(value))


#دالة ل قراءة البيانات من قاعدة البيانات 
def products(request):
     prd=product.objects.all()  #   روح اقرا كل البيانات من المودل اللي اسمها برودكت وخزنها في متغير prd
     print(prd) 
     return HttpResponse(prd)

#نرسل البيانات للصفحة الجديدة products طريقة اخرى 
def products(request):
  template=loader.get_template('products.html')
  prd=product.objects.all() 
  value={                    #قرئنا البيانات وخزناها داخل اوبجكت في مفتاح اسمه prod
     'prod':prd
     }
  return HttpResponse(template.render(value)) #اخذنا الاوبجكت وارسلناه ل صفحة اسمها products
#الخطوة اللي بعدها اروح لصفحة البرودكت  

#تجربة
def test(request):
     return HttpResponse(request.session['cart_count'])