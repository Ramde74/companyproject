from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    return render(request,'home.html')

def stdlist(request):
    std = Students.objects.all()
    return render(request,'stdlist.html',{'std':std})

def add_std(request):
    if request.method=='POST':
        print('added')

        rn = request.POST.get("rn")
        name = request.POST.get("name")
        s = Students()
        s.rn = rn
        s.name = name
        s.save()
        return redirect('std-list')
    return render(request,'addstd.html')

def delete_std(request,id):
    s=Students.objects.get(pk=id)
    s.delete()
    std = Students.objects.all()
    return render(request, 'stdlist.html', {'std': std})

def update_std(request,id):
    std = Students.objects.get(pk=id)
    return render(request,'update_std.html',{'std':std})


def do_update_std(request, id):
    rn = request.POST.get("rn")
    name = request.POST.get("name")


    s = Students.objects.get(pk=id)
    s.rn = rn
    s.name = name
    s.save()
    return redirect('std-list')


def booklist(request):
    book = Book.objects.all()
    return render(request,'booklist.html',{'book':book})

def add_book(request):
    if request.method=='POST':
        print('added')

        title = request.POST.get("title")
        author = request.POST.get("author")
        s = Book()
        s.title = title
        s.author = author
        s.save()
        return redirect('book-list')
    return render(request,'addbook.html')

def delete_book(request,id):
    s=Book.objects.get(pk=id)
    s.delete()
    book = Book.objects.all()
    return render(request, 'booklist.html', {'book': book})

def update_book(request,id):
    book = Book.objects.get(pk=id)
    return render(request,'update_book.html',{'book':book})

def do_update_book(request, id):
    title = request.POST.get("title")
    author = request.POST.get("author")


    s = Book.objects.get(pk=id)
    s.title = title
    s.author = author
    s.save()
    return redirect('book-list')

def issuelist(request):
    subject = Book_Issue.objects.all()
    return render(request,'issuelist.html',{'subject':subject})

def add_issuebook(request):
    if request.method=='POST':
        print('added')

        stu_name = request.POST.get("stu_name")
        book_name = request.POST.get("book_name")
        issue_date = request.POST.get("issue_date")
        i = Book_Issue()
        i.stu_name = stu_name
        i.book_name = book_name
        i.issue_date=issue_date
        i.save()
        return redirect('issue-list')
    return render(request,'addissuebook.html')


def delete_issuebook(request,id):
    i=Book_Issue.objects.get(pk=id)
    i.delete()
    subject = Book_Issue.objects.all()
    return render(request, 'issuelist.html', {'subject': subject})

def update_issuebook(request,id):
    subject = Book_Issue.objects.get(pk=id)
    return render(request,'update_issuebook.html',{'subject':subject})

def do_update_issuebook(request, id):
    stu_name = request.POST.get("stu_name")
    book_name = request.POST.get("book_name")
    issue_date = request.POST.get("issue_date")


    i = Book_Issue.objects.get(pk=id)
    i.stu_name = stu_name
    i.book_name = book_name
    i.issue_date = issue_date
    i.save()
    return redirect('issue-list')


