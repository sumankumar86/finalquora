from django.contrib import admin
from django.urls import path
from appsite import views
admin.site.site_header = "CDC ADMIN"
admin.site.site_title = "CDC ADMIN"
admin.site.index_title = "CDC ADMIN"


urlpatterns = [
    path('',views.signin,name='signin'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('signout/',views.signout,name='signout'),
    path('student/',views.student,name='student'),
    path('studentprofile/',views.studentprofile,name='studentprofile'),
    path('teacherprofile/',views.teacherprofile,name='teacherprofile'),
    path('cdc/',views.cdc,name='cdc'),
    path('teacher/',views.teacher,name='teacher'),
    path('forgetpassword/',views.forgetpassword,name='forgetpassword'),
    path('addquestion/',views.addquestion,name='addquestion'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('addcategory/',views.addcategory,name='addcategory'),
    path('answersubmit/<int:pk>/<int:fk>', views.answersubmit, name='answersubmit'),
 
]
