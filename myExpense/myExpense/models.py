from django import forms
from django.contrib.auth.models import User
from django.db import models
#from django.conf import settings


# Table for Category of expense.
class Category(models.Model):
    mainCategory = models.CharField('Main Category', max_length=100, null=False)
    subCategory = models.CharField('Sub Category', max_length=100, null=False)


# Table for Transactions
class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('Debit', 'Debit'),
        ('Credit', 'Credit'),
    )
    title = models.CharField('Title', max_length=100, null=False)
    description = models.CharField('Description', max_length=100, null=True)
    transType = models.CharField('Transaction Type', max_length=100, choices=TRANSACTION_TYPES, null=False)
    amount = models.FloatField(null=False)
    date = models.DateField('Transaction Date', null=False)
    #category = models.ForeignKey(Category)
    user = models.ForeignKey(User)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False)

    class Meta:
        ordering = ['date']

    def __unicode__(self):
        debugString = "Title: {0}, Description: {1}, Type: {2}, Amount: {3}, Date: {4}".format(self.title, self.description, self.transType, self.amount, self.date)
        return debugString
