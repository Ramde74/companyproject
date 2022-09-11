
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('add-std',add_std,name='add-std'),
    path('std-list',stdlist,name='std-list'),
    path('delete-std/<int:id>',delete_std,name='delete-std'),
    path('update-std/<int:id>', update_std,name='update-std'),
    path('update-std/do-update-std/<int:id>', do_update_std),
    path('book-list', booklist, name='book-list'),
    path('add-book',add_book,name='add-book'),
    path('delete-book/<int:id>',delete_book,name='delete-book'),
    path('update-book/<int:id>', update_book,name='update-book'),
    path('update-book/do-update-book/<int:id>', do_update_book),
    path('issue-list', issuelist, name='issue-list'),
    path('add-issuebook',add_issuebook,name='add-issuebook'),
    path('delete-issuebook/<int:id>',delete_issuebook,name='delete-issuebook'),
    path('update-issuebook/<int:id>', update_issuebook,name='update-issuebook'),
    path('update-issuebook/do-update-issuebook/<int:id>', do_update_issuebook),


]