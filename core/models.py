from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField('Kategori', max_length=50)
    is_delete=models.BooleanField(default=False,verbose_name = 'Sil')
    create_time = models.DateTimeField(auto_now=False, auto_now_add=True,verbose_name = 'Eklenme Zamanı')
    create_user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name = 'Kullanıcı')

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField('Adı Soyadı', max_length=50)
    age = models.IntegerField(default=0,null=True,blank=True,verbose_name = 'Yaşı')
    phone =  models.CharField('Numarası', max_length=50)
    email = models.EmailField(verbose_name="E-posta")
    address = models.CharField('Adresi', max_length=200)
    description = models.TextField(null=True,blank=True,verbose_name = 'Açıklama')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_delete=models.BooleanField(default=False,verbose_name = 'Sil')
    create_time = models.DateTimeField(auto_now=False, auto_now_add=True,verbose_name = 'Eklenme Zamanı')
    create_user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name = 'Kullanıcı')

    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Konu', max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,verbose_name="Müşteri")
    start = models.DateTimeField(verbose_name="Başlangıç")
    end = models.DateTimeField(verbose_name="Bitiş")
    is_delete=models.BooleanField(default=False,verbose_name = 'Sil')
    is_ok = models.BooleanField(default=False,verbose_name = 'Onaylandı mı ?')
    is_visit = models.BooleanField(default=False,verbose_name = 'Ziyaret edildi mi?')
    is_notificate = models.BooleanField(default=False,verbose_name = 'Bildirildi mi?')
    create_time = models.DateTimeField(auto_now=False, auto_now_add=True,verbose_name = 'Eklenme Zamanı')
    create_user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name = 'Kullanıcı')

    def __str__(self):
        return self.title+" "+self.customer.name
