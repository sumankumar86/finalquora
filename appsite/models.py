from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.

DeptChoice = [
    ('', 'Depertment'),
    ('Not Applicable', 'Not Applicable'),
    ('Mechanical', 'Mechanical'),
    ('Civil', 'Civil '),
    ('Electrical', 'Electrical'),
    ('ComputerScience', 'Computer Science'),
    ('Electronics&Communication', 'Electronics & Communication'),
]
YearChoice = [
    ('', 'Year'),
    ('Not Applicable', 'Not Applicable'),
    ('FirstYear', 'First Year'),
    ('SecondYear', 'Second Year '),
    ('ThirdYear', 'Third Year'),
    ('FourthYear', 'Fourth Year'),
]
SemChoice = [
    ('', 'Semester'),
    ('Not Applicable', 'Not Applicable'),
    ('FirstSemester', 'First Semester'),
    ('SecondSemester', 'Second Semester '),
    ('ThirdSemester', 'Third Semester'),
    ('FourthSemester', 'Fourth Semester'),
    ('FifthSemester', 'Fifth Semester'),
    ('SixthSemester', 'Sixth Semester'),
    ('SeventhSemester', 'Seventh Semester'),
    ('EightthSemester', 'Eightth Semester'),
]


class User(AbstractUser):
    # Need For All Project
    dept = models.CharField(
        max_length=40, choices=DeptChoice, default='Computer Science')
    year = models.CharField(
        max_length=40, choices=YearChoice, default='First Year')
    semester = models.CharField(
        max_length=40, choices=SemChoice, default='First Semester')
    enrollment = models.CharField(max_length=70, null=True, blank=True)
    education = models.CharField(max_length=150,null=True, blank=True)
    address = models.CharField(max_length=200,null=True, blank=True)
    skill = models.CharField(max_length=70,null=True, blank=True)
    hobby = models.CharField(max_length=100,null=True, blank=True)
    profilepic = models.ImageField(
        upload_to='profile_pic/', null=True, blank=True, default='https://res.cloudinary.com/mern-commerce/image/upload/v1633459954/usericon_hpewnq.png')
    is_cdc = models.BooleanField('Is cdc', default=False)
    is_teacher = models.BooleanField('Is teacher', default=False)
    is_student = models.BooleanField('Is student', default=False)
    status = models.BooleanField(default=True)





class QuestionCategory(models.Model):
    # Only For Quora Project
    name = models.TextField(max_length=100, null=True, blank=True)
    owner = models.PositiveIntegerField(null=True, blank=True)
    is_approve = models.BooleanField('Approve', default=False)
    is_pending = models.BooleanField('Pending', default=False)
    is_reject = models.BooleanField('Reject', default=False)
    categorytime = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)
    remarks = models.TextField(max_length=200, null=True, blank=True)


class Question(models.Model):
    # Only For Quora Project
    question = RichTextField(null=True, blank=True)
    questioncategory = models.PositiveIntegerField(null=True, blank=True)
    owner = models.PositiveIntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)
    postedtime = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)


class Answer(models.Model):
    # Only For Quora Project
    answer = models.TextField(max_length=1000)
    questionid = models.PositiveIntegerField(null=True, blank=True)
    solver = models.PositiveIntegerField(null=True, blank=True)
    answertime = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)
    status = models.BooleanField(default=True)





