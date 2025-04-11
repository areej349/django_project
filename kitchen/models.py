from django.db import models

# Create your models here.

# موديل المنتجات
class KitchenProduct(models.Model): 
    name = models.CharField(max_length=50)  # اسم المنتج
    description = models.TextField()  # وصف المنتج
    price = models.DecimalField(max_digits=10, decimal_places=2)  # السعر
    qty = models.IntegerField()  # الكمية المتوفرة
    image = models.URLField()  # رابط الصورة
    date_added = models.DateTimeField(auto_now_add=True)  # التاريخ التلقائي للإضافة

    def __str__(self):
        return self.name