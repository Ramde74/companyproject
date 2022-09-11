from django.db import models
from datetime import datetime,timedelta


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class Students(models.Model):
    rn = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name






class Book_Issue(models.Model):
    stu_name = models.ForeignKey('Students', on_delete=models.CASCADE)
    book_name = models.ForeignKey('Book', on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now=True)


