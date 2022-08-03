from django.urls import path
from .import views

urlpatterns = [
     path('',views.index,name='index'),
    path('login_page',views.login_page,name='login_page'),
    path('signup',views.signup,name='signup'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('tutor_home',views.tutor_home,name='tutor_home'),

    
    path('user_login',views.user_login,name='user_login'),
    path('logout',views.logout,name='logout'),
    path('sign_up',views.sign_up,name="sign_up"),

    path('add_course',views.add_course,name="add_course"),
    path('add_student',views.add_student,name="add_student"),

    path('course',views.course,name="course"),
    path('student',views.student,name="student"),
    path('show',views.show,name="show"),

    path('show_tutor',views.show_tutor,name="show_tutor"),
     path('show_student',views.show_student,name="show_student"),


    path('show_course',views.show_course,name="show_course"),
    path('edit_course/<int:pk>',views.edit_course,name="edit_course"),

    path('delete_course/<int:pk>',views.delete_course,name="delete_course"),

    path('edit_student/<int:pk>',views.edit_student,name="edit_student"),

    path('profile',views.profile,name="profile"),
     
    path('edit_profile',views.edit_profile,name="edit_profile"),

    path('test',views.test,name="test")




    
    
]
