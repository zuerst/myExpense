from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
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
    return render_to_response('profile/account.html', {'template': 'accont Page'})


# Rendering main page of '/add-expense' after successful login.
def addExpensePage(request):
    c = {}
    c.update(csrf(request))
    context = Context({'transactionForm': TransactionForm}, {'template': 'add Expense'})
    return render_to_response('profile/addExpense.html', c, context)


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
        category = request.POST['category']
        user = request.user
        print user
        transaction = Transaction(title = title, description = description, transType = transType, amount = amount, date = date, category = category, user = user)
        transaction.save()

    return HttpResponseRedirect('/add-expense')

# Rendering main page of '/manage-category' after successful login.
def manageCategoryPage(request):
    return render_to_response('profile/manageCategory.html', {'template': 'Category Page'})


# Rendering main page of '/report' after successful login.
def reportPage(request):
    return render_to_response('profile/report.html', {'template': 'report Page'})


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
    c = Category.objects.get(mainCategory='Drink')
    t = Transaction(title='test title', description='test description', transType='Debit', amount=100, date='2015-05-01', category=c, user=u)
    t.save()
    return render_to_response('login.html')

def test2(request):
    user = User(id=1, username="admin", is_active=True,
                is_superuser=True, is_staff=True,
                last_login="2011-09-01T13:20:30+03:00",
                email="email@gmail.com",
                date_joined="2011-09-01T13:20:30+03:00")
    user.set_password('admin')
    user.save()
    category = Category(mainCategory = "Drink", subCategory = "Coffee")
    category.save()
    return render_to_response('profile/profileMain.html')
