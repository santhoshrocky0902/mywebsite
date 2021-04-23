from django.contrib import admin
from .models import Main_Event,mci, Subscriber,mci_subcatagory
# Register your models here.

class PicAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'title')  

class Sub(admin.ModelAdmin):
    list_display = ('email', 'timestamp')  

class MCIInline(admin.StackedInline):
    model = mci_subcatagory
    extra = 1
class MCIAdmin(admin.ModelAdmin):
    inlines = [MCIInline]

admin.site.register(Main_Event, PicAdmin) 
admin.site.register(mci,MCIAdmin)
admin.site.register(Subscriber,Sub)

