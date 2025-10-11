from django.contrib import admin
from .models import Owner, House, Applicant

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact')

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'rent', 'availability')
    list_filter = ('availability', 'owner')

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'applied_house', 'status', 'income')
    list_filter = ('status',)