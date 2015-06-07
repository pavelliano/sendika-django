import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class TransactionType(models.Model):
    # id = models.IntegerField(primary_key=True)
    TYPES = (
        ('K', 'Kredi Karti'),
        ('H', 'Banka Havalesi'),
        ('E', 'Elden'),
        ('KP', 'Kredi Karti Pesin'),
        ('EP', 'Elden Pesin'),
        ('HP', 'Havale Pesin'),
    )

class Member(models.Model):
    # id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=70)
    subscription_date = models.DateTimeField('Uyelik Tarihi')
    # member_num = models.IntegerField(primary_key=True)
    # init_payment = models.ForeignKey(PaymentType)
    # debt = models.IntegerField
    # balance = models.IntegerField(default=-30)
    # last_payment = models.DateTimeField(null=True)
    def __str__(self):
        return __str__.full_name
    # def paid_debt(self):
    #     return self.last_payment >= timezone.now() - datetime.timedelta(days=30)

# class Payment(models.Model):
#     payment_made =

# class Transaction(models.Model):
#     monthly_fee = models.IntegerField('Aylik Odeme')
#
# class TransactionHistory(models.Model):
#     member_num = models.ForeignKey(Person)
#     date_of_payment = models.DateTimeField
#     price = models.IntegerField

class Transaction(models.Model):
    # id = models.IntegerField(primary_key=True)
    member_id = models.ForeignKey(Member, default='0')
    type_id = models.ForeignKey(TransactionType, default='0')
    amount = models.IntegerField(default=30)
    date = models.DateTimeField
