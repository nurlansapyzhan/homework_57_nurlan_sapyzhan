from django.contrib import admin

from hw57.models import Type, Status, Issue


# Register your models here.
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    fields = ('id', 'name')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    fields = ('id', 'name')


class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'description', 'status', 'created_date', 'updated_date')
    list_filter = ('id', 'summary', 'description', 'status', 'type')
    search_fields = ('status', 'type', 'finish_date', 'updated_date')
    fields = ('id', 'summary', 'description', 'status', 'created_date', 'updated_date')
    readonly_fields = ('id', 'created_date', 'updated_date')


admin.site.register(Type, TypeAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Issue, IssueAdmin)
