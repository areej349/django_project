from django.db import models

# Create your models here.
#model_1
class product(models.Model): 
    name=models.CharField(max_length=50) #string
    color=models.CharField(max_length=50) #string
    price=models.DecimalField(max_digits=10,decimal_places=5) #decimal وحددت ديسمال ادق بالعمليات الحسابية - حددت المنازل
    qty=models.IntegerField() #int
    tax=models.FloatField()
    total=models.DecimalField(max_digits=10,decimal_places=5)
    date=models.DateTimeField(auto_now_add=True) # التاريخ تلقائي
    

# دالة بسيطة عشان اظهر المودل في صفحة التحكم او admin  
    def __str__(self):
        return self.name


#model_2

class electronic(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    notes=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
