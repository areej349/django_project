"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from home import views as _home
from electronic import views as _electronic
from kitchen import views as _kitchen
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #مسارات الالكترونيات
    path('admin/', admin.site.urls),
    path('', _home.showland ,name='index'),
    path('electronic/' , _electronic.list_electronic, name='list_electronic'),
    path('showphone/<str:phone>/' , _electronic.showphone, name='showphone'), #لان الدالة تستقبل براميتر نعرفه هنا 
    path('categories/' , _electronic.categories, name='categories'),
    path('products/',_electronic.products), # اذا جا طلب برودكت روح استدعي الدالة برودكت 

   #مسارات ادوات المطبخ
    path('list_kitchen/', _kitchen.list_kitchen, name='list_kitchen'),  
    path('kitchen/product/<int:item_id>/', _kitchen.show_kitchen, name='show_kitchen'),  # عرض تفاصيل المنتج

#مسارات الهوم
    path('list_product/<int:id>',_home.list_product,name='list_product'),
    path('details/<int:id>' , _home.product_details, name='details'),
    path('addtocart/',_home.add_to_cart,name='addtocart'),
    path('test/',_electronic.test),    #تجربة
    path('checkout/', _home.checkout,name='checkout'),

#ربط url خاص في تطبيق مع الurl الاساسي للمشروع كامل   
#ربط url داخلي مع الurl الخارجي 
    path('accounts/',include('accounts.urls')),

    path('get_api/' ,_home.get_api,name='get_api'),

    #invoice
    path('process-payment/', _home.process_payment, name='process_payment'),


    path('search/', _home.search, name='search'),  # تغيير من 'index' إلى 'search'


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
