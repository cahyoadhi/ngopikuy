from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

class Profile(models.Model):
    user = models.OneToOneField(User, null= True, blank= True, on_delete=models.CASCADE)
    name = models.CharField(max_length= 40, null= True, blank= True)
    email = models.CharField(max_length= 40, null= True, blank= True)
    phone = models.CharField(max_length= 40, null= True, blank= True)
    profile_pic = models.ImageField()
    def __str__(self):
        return str(self.user) 

    @property
    def pictUrl(self):
        try:
            url = self.profile_pic
        except:
            url = ''
        return url        

class Product(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='product', null=True, blank=True)

    def __str__(self):
        return self.name
    tags = TaggableManager()

    @property
    def priceCurrency(self):
        total = '{:20,.2f}'.format(self.price)
        return total

    @property
    def priceNominal(self):
        total = float(self.price)/ 1000.0
        return total

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank= True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.quantity} of {self.product.name} created by {self.user}"
    
    @property
    def totalPrice(self):
        total = self.product.price * self.quantity
        return total
    
    @property
    def totalPriceNominal(self):
        total = float(self.totalPrice)/ 1000.0
        return total

    @property
    def grandTotalPrice(self):
        total = 0
        for userorder in self.product.all():
            total += userorder.totalPrice()
        return total        

class Order(models.Model):
    ORDER_STATS = [
    ('New-Order', 'New-Order'),
    ('Process', 'Process'),
    ('Complete', 'Complete'),
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    payment = models.CharField(max_length=100, blank=True, null=True)
    customer = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(choices=ORDER_STATS, default="New-Order", max_length=30)
    tracking_no = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    created_add = models.DateTimeField(auto_now_add=True)
    completed_times = models.DateTimeField(blank=True, null=True)
    total_price = models.IntegerField(blank=True, null=True)
    list_order_json = models.JSONField(null=True)

    def __str__(self):
        return self.tracking_no


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    statss = ((0,"Draft"),(1,"Publish"))
    status = models.IntegerField(choices=statss, default=0)
    thumbnail = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title       

    @property
    def thumbnailUrl(self):
        try:
            url = self.thumbnail.url
        except:
            url = ''
        return url
