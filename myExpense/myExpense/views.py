from django.contrib import auth
from django.core import serializers
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import Context, loader, RequestContext

from forms import RegistrationForm
from models import *

############################
# Main Page
############################


# Rendering the main page '/'
def mainPage(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('mainPage.html', c)

############################
# Profile Main Page
############################


# Rendering main page of '/profile' after successful login.
def profilePage(request):
    return render_to_response('profile/profileMain.html', {'template': 'Main Page'})


# Rendering main page of '/account' after successful login.
def accountPage(request):
    userID = request.user.id
    user = User.objects.get(id = userID)
    return render_to_response('profile/account.html', {'user': user})


# Rendering main page of '/add-expense' after successful login.
def addExpensePage(request):
    c = {}
    c.update(csrf(request))
    c['transactionForm'] = TransactionForm
    user = request.user
    filteredCats = Category.objects.filter(user = user.id)
    c['filteredCats'] = filteredCats
    recentList = Transaction.objects.filter(user = user.id)[:7]
    c['recentList'] = recentList
    if request.method == 'POST':
        if request.POST['method'] == "delete":
            transID = request.POST['transID']
            target = Transaction.objects.get(transID = transID)
            target.delete()
            return render_to_response('profile/addExpense.html', c)
    return render_to_response('profile/addExpense.html', c)


# Helper function for addExpensePage.
# Add expense when button is clicked.
def addExpense(request):
    if request.method == 'POST':
        print request.POST
        title = request.POST['title']
        description = request.POST['description']
        transType = request.POST['transType']
        amount = request.POST['amount']
        date = request.POST['date']
        color = request.POST['color']
        catName = request.POST.get('category', 1)
        userID = request.user.id
        category = Category.objects.filter(catName = catName, color = color, user = userID)
        print category
        category = category[0]
        user = User.objects.get(id = userID)
        transaction = Transaction(title = title, description = description, transType = transType, amount = amount, date = date, category=category, user= user)
        transaction.save()

    return HttpResponseRedirect('/profile/add-expense')

def deleteHistory(request):
    pass

def editEntry(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        transType = request.POST['transType']
        amount = request.POST['amount']
        date = request.POST['date']
        color = request.POST['color']
        catName = request.POST.get('category', 1)
        userID = request.user.id
        category = Category.objects.filter(catName = catName, color = color, user = userID)
        category = category[0]
        user = User.objects.get(id = userID)
        transaction = Transaction(title = title, description = description, transType = transType, amount = amount, date = date, category = category, user = user)
        transaction.save()

    return HttpResponseRedirect('/profile/add-expense')
    
# Rendering main page of '/manage-category' after successful login.
def manageCategoryPage(request):
    categories = Category.objects.all()
    return render_to_response('profile/manageCategory.html', {'categories': categories})


# Rendering main page of '/report' after successful login.
def reportPage(request):
    c = {}
    c.update(csrf(request))
    transactions = Transaction.objects.all()
    c['transactions'] = transactions
    if request.method == 'POST':
        startDate = request.POST.get('startDate', '')
        endDate = request.POST.get('endDate', '')
        queryList = Transaction.objects.filter(date__gte=startDate, date__lte=endDate)
        queryJSON = serializers.serialize('json', queryList)
        print queryJSON
        return HttpResponse(content=queryJSON, content_type="application/json", status=200)
        # return HttpResponse(status=200)
    else:
        return render_to_response('profile/report.html', c)


############################
# Login and Register
############################


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile')
    else:
        c = {}
        c.update(csrf(request))
        c.update({'nextURL': request.GET.get('next', '/profile')})
        return render_to_response('profile/profileLogin.html', c)


def auth_view(request):
    # GET username, if there is no valid data, return ''.
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    nextURL = request.POST.get('next', '/profile')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(nextURL)
    else:
        return HttpResponseRedirect('/accounts/invalid_login')


def loggedin(request):
    c = {}
    c.update(csrf(request))
    c['username'] = request.user.username
    return HttpResponseRedirect('/profile')


def invalid_login(request):
    return render_to_response('accounts/invalid_login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('accounts/logout.html')


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        else:
            return render_to_response('accounts/register.html', {'form': form})
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm()
    return render(request, 'accounts/register.html', args)


def register_success(request):
    return render_to_response('accounts/register_success.html')


################################################
# Requets for creating Test Cases
################################################

# Creating some test case.
def test(request):
    u = User.objects.get(id=1)
    c = Category.objects.filter(catName='Drink')[0]
    t = Transaction(title='test title', description='test description', transType='Debit', amount=100, date='2015-05-01', category=c, user=u)
    for i in range(1,10):
        trans = Transaction(title='test title {0}'.format(i), description='test description {0}'.format(i), transType='Debit', amount=100 + i, date='2015-05-{0}'.format(i), category=c, user=u)
        trans.save()
    t.save()
    return render_to_response('profile/profileMain.html')

def test2(request):
    user = User(id=1, username="admin", is_active=True,
                is_superuser=True, is_staff=True,
                last_login="2011-09-01T13:20:30+03:00",
                email="email@gmail.com",
                date_joined="2011-09-01T13:20:30+03:00")
    user.set_password('admin')
    user.save()
    category = Category(catName = "Drink", color = "blueButton", user = user)
    category.save()

    return render_to_response('profile/profileMain.html')
