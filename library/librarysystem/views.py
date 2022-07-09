from django.db.models.fields import NullBooleanField
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, request
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.


def demohome(request):
    print(request.session.get('user_id'))
    if request.method == 'GET':
        email = request.GET.get('Email')
        password = request.GET.get('Password')
    emails = Profile.objects.all()
    for x in emails:
        if x.email == email and x.password == password:
            print(x.ProfileID)
            request.session['user_id'] = x.ProfileID
            return redirect('Student')
        else:
            print("false")
    return render(request, 'pages\\home.html')


def demoaboutus(request):
    return render(request, 'pages\\aboutus.html')


def addbook(request):
    header = request.POST.get('titleofthebook')
    author = request.POST.get('nameofauthor')
    id = request.POST.get('ide')
    isbn = request.POST.get('isbn')
    active = request.POST.get('Active')
    publishery = request.POST.get('pub')
    Publication_Yeary = request.POST.get('pubyear')
    categoryy = request.POST.get('cat')
    if header is not None:
        data = Book(title=header, author=author, ISBN=isbn, ID=id,
                    Publisher=publishery, Publication_Year=Publication_Yeary, Category=categoryy)
        data.save()
        return redirect('home')
    return render(request, 'pages\\addbook.html')

# data = book.objects.get(title = variable)


def democontact(request):
    return render(request, 'pages\\contactus.html')


def demosearch(request):
    return render(request, 'pages\\searchbook.html')


def demostudent(request):
    return render(request, 'pages\\asstudent.html')


def demoupdateuser(request):
    context = {'Profile': Profile.objects.all()}
    return render(request, 'pages\\demoupdate.html',context)


def demoborrow(request):
    return render(request, 'pages\\borrow.html')


def borrowabook(request):
    time = request.POST.get('time')
    id = request.POST.get('id')
    if time is not None:
        book = Book.objects.get(ID=id)
        book.borrowing_period = time
        book.save()
        redirect('Borrow')
    return render(request, 'pages\\borrow.html', {'ListBooks': Book.objects.all()})


def returnabook(request):
    id = request.GET.get('id')
    book = Book.objects.get(ID=id)
    book.status = True
    book.save()
    return redirect('listall')


def demoupdatespecbook(request):
    return render(request, 'pages\\newspecbook.html')


def demolist(request):
    search = Book.objects.all()
    search_value = request.GET['search']
    if not search_value:
        pass  # TODO: handle empty search

    if request.GET['type'] == 'isbn':
        search = search.filter(ISBN=search_value)

    if request.GET['type'] == 'author':
        search = search.filter(author=search_value)

    if request.GET['type'] == 'title':
        search = search.filter(title=search_value)

    if request.GET['type'] == 'year':
        search = search.filter(year=search_value)

    context = {
        'ListBooks': search

    }
    return render(request, 'pages\\listbooks.html', context)


def demoadmin(request):
    return render(request, 'pages\\asadmin.html')


def demoupdatebook(request):
    update = Book.objects.all()
    context = {
        'UpdateBook': Book.objects.all()
    }

    return render(request, 'pages\\newbook.html', context)


def updatebook(request):

    return redirect('list')


def democontactadmin(request):
    return render(request, 'pages\\admincontactus.html')


def democontactstudent(request):
    return render(request, 'pages\\studentcontactus.html')


def demolistall(request):
    id = request.POST.get('id')
    clock = request.POST.get('time')
    if clock is not None:
        book = Book.objects.get(ID=id)
        book.status = False
        book.borrowing_period = clock
        book.save()
        return redirect('listall')
    return render(request, 'pages\\listbooks.html', {'ListBooks': Book.objects.all()})


def Signup(request):
    username = request.POST.get('UName')
    Birth_Date = request.POST.get('DoB')
    address = request.POST.get('add')
    city = request.POST.get('city')
    num = request.POST.get('phone')
    email = request.POST.get('email')
    password = request.POST.get('pass')
    profileID = request.POST.get('id')

    if username is not None:

        data = Profile(username=username, birthDate=Birth_Date, address=address,
                       city=city, mobile=num, email=email, password=password,profileID=profileID)
        data.save()

    return render(request, 'pages\\Register.html')

def update(request,ID):
        bookID= Book.objects.get(ID=ID)
        if request.method== 'POST':
            book_save=BookForm(request.POST, request.FILES, instance=bookID)
            if book_save.is_valid():
                book_save.save()
        else:
            book_save= BookForm(instance=bookID)
        context={
            'form': book_save
        }
        return render(request,'pages/newspecbook.html', context)


def newuser(request,id):
    try:
        user_id = Profile.objects.get(profileID = id)
    except Profile.DoesNotExist:
        user_id = None
    if request.method == 'POST':
        update_user = UserForm(request.POST, instance=user_id)
        if update_user.is_valid():
            update_user.save()
            return redirect('newuser', id)
    else:
        update_user = UserForm(instance=user_id)

    context = {
        'userForm': update_user,
        'userId': id,
    }
    return render(request, 'pages/newuser.html', context)