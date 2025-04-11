from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=50)
    icon=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Product(models.Model): 
    name=models.CharField(max_length=50) #string
    color=models.CharField(max_length=50) #string
    price=models.DecimalField(max_digits=10,decimal_places=5) #decimal وحددت ديسمال ادق بالعمليات الحسابية - حددت المنازل
    qty=models.IntegerField() #int
    tax=models.FloatField()
    total=models.DecimalField(max_digits=10,decimal_places=5)
    date=models.DateTimeField(auto_now_add=True) # التاريخ تلقائي
    image = models.ImageField(upload_to='images/')  #الصور راح تتحمل لمجلد اسمهimages
    categories=models.ForeignKey(Categories,on_delete=models.CASCADE) #مفتاح اجنبي____  #ربط جدول البرودكت مع الكاتقري  #اون ديليت يعني اذا تم حذف سجل في الكاتقري راح ينحذف نفس السجل المربط بالجدول الاخر
# دالة بسيطة عشان اظهر المودل في صفحة التحكم او admin  
    def __str__(self):
        return self.name
    

    #invoice 
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    

