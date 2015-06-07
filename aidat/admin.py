from django.contrib import admin

# Register your models here.
from .models import TransactionType, Member, Transaction

class MemberInline(admin.TabularInline):
     model = Member
     extra = 3


class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields':['full_name']}),
        ('Date information', {'fields':['subscription_date'], 'classes':['collapse']}),
    ]
    inlines = [MemberInline]
    # list_display = ('subscription_date', 'last_payment', 'was_published_recently')
    # list_filter = ['paid_debt']
    # search_fields = ['full_name']



admin.site.register(Member)
# admin.site.register(Choice)
