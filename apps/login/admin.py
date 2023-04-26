from django.contrib import admin
from .models import *
# Register your models here.
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', "post_time","content")



admin.site.register(Comments,CommentsAdmin)


class New_memberAdmin(admin.ModelAdmin):
    # 定制哪些字段需要展示
    list_display = ('id', 'name', 'sex', "major", "department", "phone_number", "email", "expectation", "status")

    list_filter = ('sex', 'department', "status")

    list_editable = ('status', "department")

    search_fields = ['name']

    empty_value_display = 'NA'


admin.site.register(NewMember, New_memberAdmin)



class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id","department_cn","department_en","icon","background","status")

class HistoryAdmin(admin.ModelAdmin):
    list_display = ("id","years","department")

class MembersAdmin(admin.ModelAdmin):
    list_display = ("id","years","name","motto","department")
admin.site.register(Department,DepartmentAdmin)
admin.site.register(History,HistoryAdmin)
admin.site.register(Members,MembersAdmin)



class WorksAdmin(admin.ModelAdmin):
    list_display = ("grade","name","description","img")

admin.site.register(Works,WorksAdmin)
