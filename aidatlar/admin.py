from django.contrib import admin

# Register your models here.
# from .models import PaymentType, Person, Transaction
#
# class PersonInline(admin.TabularInline):
#      model = Person
#      extra = 3
#
#
# class PersonAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields':['full_name']}),
#         ('Date information', {'fields':['subscription_date'], 'classes':['collapse']}),
#     ]
#     inlines = [PersonInline]
#     list_display = ('subscription_date', 'last_payment', 'was_published_recently')
#     list_filter = ['paid_debt']
#     search_fields = ['full_name']
#
#
#
# admin.site.register(Person)
# admin.site.register(Choice)
