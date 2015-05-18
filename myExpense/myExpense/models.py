from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm


class Group(models.Model):
    COLOR_TYPES = (
        ('whiteButton', 'whiteButton'),
        ('redButton', 'redButton'),
        ('blueButton', 'blueButton'),
        ('greenButton', 'greenButton'),
        ('tealButton', 'tealButton'),
        ('orangeButton', 'orangeButton'),
    )
    name = models.CharField('Group Name', max_length=100, null=False)
    description = models.CharField('Group Name', max_length=300, null=False, blank=True)
    transaction = models.ManyToManyField('Transaction', null=True, blank=True)
    user = models.ManyToManyField(User, null=True, blank=True)
    lastUpdated = models.DateTimeField('Last Updated', null=False)
    color = models.CharField('Color', max_length=100, choices=COLOR_TYPES, null=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-lastUpdated']

# Table for Category of expense.
class Category(models.Model):
    COLOR_TYPES = (
        ('whiteButton', 'whiteButton'),
        ('redButton', 'redButton'),
        ('blueButton', 'blueButton'),
        ('greenButton', 'greenButton'),
        ('tealButton', 'tealButton'),
        ('orangeButton', 'orangeButton'),
    )
    catNum = models.AutoField('Category Num', max_length=8, primary_key=True)
    catName = models.CharField('Category Name', max_length=100, null=False)
    color = models.CharField('Color', max_length=100, choices=COLOR_TYPES, null=False)
    user = models.ForeignKey(User)

    def __unicode__(self):
        catInfo = self.catName
        return catInfo

    class Meta:
        ordering = ['catName']
        
    def __unicode__(self):
       return self.catName

# Table for Transactions
class Transaction(models.Model):
    transID = models.AutoField('Transaction ID', max_length=8, primary_key=True)
    TRANSACTION_TYPES = (
        ('+', '+'),
        ('-', '-'),
    )
    title = models.CharField('Title', max_length=100, null=False)
    description = models.CharField('Description', max_length=100, null=True)
    transType = models.CharField('Transaction Type', max_length=100, choices=TRANSACTION_TYPES, null=False)
    amount = models.FloatField(null=False)
    transactionTime = models.DateTimeField('Transaction Time', null=False)
    category = models.ForeignKey(Category)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-transactionTime']

    def __unicode__(self):
        debugString = "Title: {0}, Description: {1}, Type: {2}, Amount: {3}, Time: {4}".format(self.title, self.description, self.transType, self.amount, self.transactionTime)
        return debugString


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'description', 'transType', 'amount', 'transactionTime', 'category']
