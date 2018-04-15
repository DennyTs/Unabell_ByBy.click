from django.contrib import admin

from backend.models import UserProfile,Button, Regist, Product, Bundle, Record

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Button)
admin.site.register(Regist)
admin.site.register(Product)
admin.site.register(Bundle)
admin.site.register(Record)