from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'id', 'email', 'dept', 'year', 'semester',
                    'enrollment', 'profilepic',
                    'is_cdc', 'is_teacher', 'is_student', 'status']


@admin.register(QuestionCategory)
class QuestionCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'owner','categorytime','is_approve','is_pending','is_reject','remarks']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'questioncategory',
                    'owner', 'status', 'postedtime']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'answer', 'questionid',
                    'solver', 'answertime', 'status']


