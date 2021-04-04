from django.contrib import admin
from .models import New,Event, indexvideo, gallery, Main_facility, Sspeciality, Clinical


class FacilityAdmin(admin.ModelAdmin):
    list_display=['get_Name_display']
    
admin.site.register(New)  

admin.site.register(Event)  

admin.site.register(indexvideo) 

admin.site.register(gallery) 

admin.site.register(Main_facility,FacilityAdmin)  

admin.site.register(Sspeciality,FacilityAdmin)  

admin.site.register(Clinical,FacilityAdmin)  