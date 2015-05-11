from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
#from django.conf import settings


# Table for Category of expense.
class Category(models.Model):
    catNum = models.AutoField('Category Num', max_length=8, primary_key=True)
    mainCategory = models.CharField('Main Category', max_length=100, null=False)
    subCategory = models.CharField('Sub Category', max_length=100, null=False)

    class Meta:
        ordering = ['mainCategory']
        
    def __unicode__(self):
        categoryString = "{0}: {1}".format(self.mainCategory, self.subCategory)
        return categoryString

# Table for Transactions
class Transaction(models.Model):
    transID = models.AutoField('Transaction ID', max_length=8, primary_key=True)
    TRANSACTION_TYPES = (
        ('Debit', 'Debit'),
        ('Credit', 'Credit'),
    )
    title = models.CharField('Title', max_length=100, null=False)
    description = models.CharField('Description', max_length=100, null=True)
    transType = models.CharField('Transaction Type', max_length=100, choices=TRANSACTION_TYPES, null=False)
    amount = models.FloatField(null=False)
    date = models.DateField('Transaction Date', null=False)
    category = models.ForeignKey(Category, default=1)
    user = models.ForeignKey(User, default=1)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False)

    class Meta:
        ordering = ['date']

    def __unicode__(self):
        debugString = "Title: {0}, Description: {1}, Type: {2}, Amount: {3}, Date: {4}".format(self.title, self.description, self.transType, self.amount, self.date)
        return debugString


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'description', 'transType', 'amount', 'date', 'category']
