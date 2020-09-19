from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing_page,name='login_page'),
    path('student',views.student_page,name='student_page'),
    path('teacher',views.teacher_main,name='teacher_page'),
    path('create/<str:mail>',views.teacher_create.as_view(),name='teacher_create'),
    path('list',views.teacher_list,name='teacher_list'),
    path('detail',views.teacher_detail.as_view(),name='teacher_detail'),
    path('studentscore', views.teacher_view, name='teacher_view')
]
