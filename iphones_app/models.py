from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=20,verbose_name='Contacter_Name',blank=False,null=True)
    email = models.EmailField(verbose_name='Contacter_Email',blank=False,null=True)
    phone_number = models.CharField(max_length=20,verbose_name='Contacter_Phone_Number',blank=False,null=True)
    message = models.TextField(verbose_name='Contacter',blank=False,null=True)
    create_data = models.DateTimeField(auto_now_add=True,null=True)
    update_data = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-create_data','-update_data']



class Brand(models.Model):
    name= models.CharField(max_length=20,verbose_name='Brand_Name')
    img = models.ImageField(upload_to="Brand_img")
    create_data = models.DateTimeField(auto_now_add=True,null=True)
    update_data = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-create_data','-update_data']


class Product(models.Model):

    COLORS = [
        ('blue','blue'),
        ('dark-blue','dark-blue'),
        ('grey','grey'),
        ('golden','golden'),
        ('black','black'),
        ('red','red'),
        ('white','white'),
        ('green','green'),
    ]

    title = models.CharField(max_length=50,verbose_name="Name product", blank = False)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL,verbose_name="Brand", null=True)    
    image = models.ImageField(upload_to="Product_img",verbose_name="image", blank = False,null=True )
    price = models.FloatField(default="0.00",verbose_name="price", blank = False,null=True)
    quant = models.IntegerField(default="5",verbose_name="quant", blank = False,null=True)
    description = models.TextField(verbose_name="description", blank = False)
    color = models.CharField(verbose_name='Color',choices=COLORS,max_length=50,blank=True,null=True)
    create_data = models.DateTimeField(auto_now_add=True,null=True)
    update_data = models.DateTimeField(auto_now=True,null=True)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-create_data','-update_data']


class Opinion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.TextField(verbose_name="description", blank = False,null=True)
    create_data = models.DateTimeField(auto_now_add=True,null=True)
    update_data = models.DateTimeField(auto_now=True,null=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE,verbose_name="product", blank=True, null=True)
        
    def __str__(self):  
        return self.user.username

    class Meta:
        ordering = ['-create_data','-update_data']

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Brand", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default="0.00",verbose_name="price", blank = False,null=True)
    quant = models.IntegerField(default="5",verbose_name="quant", blank = False,null=True)
    create_data = models.DateTimeField(auto_now_add=True,null=True)
    update_data = models.DateTimeField(auto_now=True,null=True)

    # brand  = models.ForeignKey(Brand, on_delete=models.SET_NULL,verbose_name="Brand", null=True)    
    # title= models.CharField(max_length=50,verbose_name="Name product", blank = False)
    # description = models.TextField(verbose_name="description", blank = False)
    # image = models.ImageField(upload_to="Product_img",verbose_name="image", blank = False,null=True )
    # color = models.CharField(verbose_name='Color',max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.product
    
    class Meta:
        ordering = ['-create_data','-update_data']


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name="Brand", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default="0.00",verbose_name="price", blank = False,null=True)
    quant = models.IntegerField(default="5",verbose_name="quant", blank = False,null=True)
    create_data = models.DateTimeField(auto_now_add=True,null=True)
    update_data = models.DateTimeField(auto_now=True,null=True)   

    # brand  = models.CharField(verbose_name="Brand", max_length=100,null=True)    
    # title= models.CharField(max_length=50,verbose_name="Name product", blank = False)
    # description = models.TextField(verbose_name="description", blank = False)
    # image = models.ImageField(upload_to="Product_img",verbose_name="image", blank = False,null=True )
    # color = models.CharField(verbose_name='Color',max_length=50,blank=True,null=True)
    # product = models.CharField(verbose_name="Product", max_length=100,null=True)

    def __str__(self):
        return self.product
    
    class Meta:
        ordering = ['-create_data','-update_data']


class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name="Brand", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.FloatField(default="0.00",verbose_name="price", blank = False,null=True)
    create_data = models.DateTimeField(auto_now_add=True,null=True)
    update_data = models.DateTimeField(auto_now=True,null=True)
    # brand  = models.ForeignKey(Brand, on_delete=models.SET_NULL,verbose_name="Brand", null=True)    
    # title= models.CharField(max_length=50,verbose_name="Name product", blank = False)
    # description = models.TextField(verbose_name="description", blank = False)
    # image = models.ImageField(upload_to="Product_img",verbose_name="image", blank = False,null=True )
    # color = models.CharField(verbose_name='Color',max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.product
    
    class Meta:
        ordering = ['-create_data','-update_data']



