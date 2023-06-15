from django.db import models

# Create your models here.

class ProductCatagory(models.Model):
    Catagory=models.CharField(max_length=100)
    cid=models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.Catagory

class Products(models.Model):
    Catagory=models.ForeignKey(ProductCatagory,on_delete=models.CASCADE)
    pname=models.CharField(max_length=100)
    prise=models.DecimalField(max_digits=6,decimal_places=3)
    pid=models.IntegerField()
    date=models.DateField()

    def __str__(self) -> str:
        return self.pname

