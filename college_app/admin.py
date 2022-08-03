from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Course)




@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','Student_Name','Address','Age','Join_date','Course')


admin.site.register(Tutor)    