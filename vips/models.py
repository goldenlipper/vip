from django.contrib.auth.models import User
from django.db import models


class GlUser(models.Model):
    sex_choices = (
        ('unknown', 'unknown'),
        ('m', 'male'),
        ('f', 'female'),
    )
    GL_customer = models.OneToOneField(User, on_delete=models.CASCADE)
    GL_username = models.CharField(max_length=50, default='')
    GL_address = models.CharField(max_length=100, default='')
    GL_sex = models.CharField(max_length=20, choices=sex_choices, default='unknown')
    GL_birthday = models.DateField(max_length=20, default='')
    GL_email = models.EmailField(max_length=50, default='')
    contact = models.CharField(max_length=100, default='')

    def __str__(self):
        return 'Customer name: ' + self.GL_username


class Vip1(models.Model):
    customer = models.OneToOneField('GlUser', on_delete=models.CASCADE)
    customer_level_number = models.CharField(max_length=20, default='1')
    total_amount = models.ManyToManyField('Selling', blank=True)
    lower_vip = models.OneToOneField('VipGroup', on_delete=models.CASCADE, blank=True, null=True)

    def getTotal(self):
        total = 0
        for sell in self.total_amount.all():
            total += sell.amount
        return total

    def getAllTotal(self):
        total = 0
        total += self.getTotal()
        for seller in self.lower_vip.vip_group.all():
            sellings = Selling.objects.filter(seller=seller)
            for selling in sellings:
                total += selling.amount
        return total

    def __str__(self):
        return 'Level1 Customer name: ' + self.customer.GL_username


class Vip2(models.Model):
    customer = models.OneToOneField('GlUser', on_delete=models.CASCADE)
    customer_level_number = models.CharField(max_length=20, default='2')
    total_amount = models.ManyToManyField('Selling', blank=True)
    lower_vip = models.OneToOneField('VipGroup', on_delete=models.CASCADE, blank=True, null=True)
    higher_vip = models.ForeignKey('Vip1', on_delete=models.SET_NULL, blank=True, null=True)

    def getTotal(self):
        total = 0
        for sell in self.total_amount.all():
            total += sell.amount
        return total

    def getAllTotal(self):
        total = 0
        total += self.getTotal()
        for seller in self.lower_vip.vip_group.all():
            sellings = Selling.objects.filter(seller=seller)
            for selling in sellings:
                total += selling.amount
        return total

    def __str__(self):
        return 'Level2 Customer name: ' + self.customer.GL_username


class Vip3(models.Model):
    customer = models.OneToOneField('GlUser', on_delete=models.CASCADE)
    customer_level_number = models.CharField(max_length=20, default='3')
    total_amount = models.ManyToManyField('Selling', blank=True)
    lower_vip = models.OneToOneField('VipGroup', on_delete=models.CASCADE, blank=True, null=True)
    higher_vip = models.ForeignKey('Vip2', on_delete=models.SET_NULL, blank=True, null=True)

    def getTotal(self):
        total = 0
        for sell in self.total_amount.all():
            total += sell.amount
        return total

    def getAllTotal(self):
        total = 0
        total += self.getTotal()
        for seller in self.lower_vip.vip_group.all():
            sellings = Selling.objects.filter(seller=seller)
            for selling in sellings:
                total += selling.amount
        return total

    def __str__(self):
        return 'Level3 Customer name: ' + self.customer.GL_username


class Vip4(models.Model):
    customer = models.OneToOneField('GlUser', on_delete=models.CASCADE)
    customer_level_number = models.CharField(max_length=20, default='4')
    total_amount = models.ManyToManyField('Selling', blank=True)
    higher_vip = models.ForeignKey('Vip3', on_delete=models.SET_NULL, blank=True, null=True)

    def getTotal(self):
        total = 0
        for sell in self.total_amount.all():
            total += sell.amount
        return total

    def getAllTotal(self):
        total = 0
        total += self.getTotal()
        return total

    def __str__(self):
        return 'Level4 Customer name: ' + self.customer.GL_username


class Selling(models.Model):
    amount = models.FloatField(default=0.0)
    date = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey('GlUser', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.date.day) + "\n" + str(self.amount) + "\n" + str(self.seller)


class VipGroup(models.Model):
    group_name = models.CharField(max_length=100, default='')
    vip_group = models.ManyToManyField('GlUser')

    def __str__(self):
        return self.group_name
