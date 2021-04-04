from django.contrib import admin
from .models import Main_Event,mci, Subscriber
# Register your models here.

class PicAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'title')  

class Sub(admin.ModelAdmin):
    list_display = ('email', 'timestamp')  


admin.site.register(Main_Event, PicAdmin) 
admin.site.register(mci)
admin.site.register(Subscriber,Sub)

