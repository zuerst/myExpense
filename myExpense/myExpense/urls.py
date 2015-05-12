"""myExpense URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # URL for admin account
    url(r'^admin/', include(admin.site.urls)),

    # Main page for my Expense
    url(r'^$', 'myExpense.views.mainPage'),

    # Main profile page (Successful login)
    url(r'^profile$', 'myExpense.views.profilePage'),
    url(r'^profile/account$', 'myExpense.views.accountPage'),
    url(r'^profile/add-expense$', 'myExpense.views.addExpensePage'),
    url(r'^profile/addingExpense$', 'myExpense.views.addExpense'),
    url(r'^profile/manage-category$', 'myExpense.views.manageCategoryPage'),
    url(r'^profile/report$', 'myExpense.views.reportPage'),
    url(r'^profile/transControl$', 'myExpense.views.transControl'),

    # URL for Login and Register User.
    url(r'^accounts/login/$', 'myExpense.views.login'),
    url(r'^accounts/auth/$', 'myExpense.views.auth_view'),
    url(r'^accounts/loggedin/$', 'myExpense.views.loggedin'),
    url(r'^accounts/invalid_login/$', 'myExpense.views.invalid_login'),
    url(r'^accounts/logout/$', 'myExpense.views.logout'),
    url(r'^accounts/register/$', 'myExpense.views.register_user'),

    # Some Test urls Adding simple data into Transaction table.
    url(r'^test/', 'myExpense.views.test'),
    url(r'^test2/', 'myExpense.views.test2'),
]
