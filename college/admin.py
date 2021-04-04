from django.contrib import admin
from django.forms import TextInput, Textarea
import nested_admin

from .models import New,Event,Department,Achievement,best_moments,Awards,HOD,Professor,Facility,Gallery, Main_facility, Hyperlink, PaperPublication,OnlineApplication

from django.db import models

admin.site.register(New)  

admin.site.register(Event)  

class MeasurementMethodAdmin(admin.ModelAdmin):
  def has_module_permission(self, request):
    return False

class AchievementInline(admin.StackedInline):
    model = Achievement
    extra = 1

class BestMomentInline(admin.StackedInline):
    model = best_moments
    extra = 3

class AwardsInline(admin.StackedInline):
    model = Awards
    extra = 1
class HODInline(admin.StackedInline):
    model = HOD
    extra = 1
class ProfessorInline(admin.StackedInline):
    model = Professor
    extra = 1
class FacilityInline(admin.StackedInline):
    model = Facility
    extra = 1
class GalleryInline(admin.StackedInline):
    model = Gallery
    extra = 1

class PaperPublicationInline(admin.StackedInline):
    model = PaperPublication
    extra = 1

class HyperlinkInline(admin.StackedInline):
    model = Hyperlink
    extra = 2




class PersonAdmin(admin.ModelAdmin):
    list_display=['get_Name_display']
    inlines = [AchievementInline,BestMomentInline,AwardsInline,HODInline,ProfessorInline,FacilityInline,GalleryInline, PaperPublicationInline]

class FacilityAdmin(admin.ModelAdmin):
    list_display=['get_Name_display']
    inlines = [HyperlinkInline]

class AdmissionAdmin(admin.ModelAdmin):
    list_display =['applicant_name', 'has_enquired']
    fieldsets = (
            (None, {
                'fields': ('degree', 'image','year', 'course_type','branch')
            }),
            ('Personal Information', {
                'fields': ('applicant_name', 'date_of_birth','age','blood_group','mother_tounge',
                'religion','cast','community','reserved_category','physically_handicapped'),
            }),
            ('Parents Information', {
                'fields': ('father_name', 'father_occupation','father_income','mother_name','mother_occupation',
                'mother_income','gaurdian_name','gaurdian_occupation','gaurdian_income'),
            }),
            ('Student Details', {
                'fields': ('nationality', 'native_place','state','email','phone')
            }),
            ('Parents Details', {
                'fields': ('currrent_address_line1', 'current_address_line2','current_city','current_pincode','current_phone',
                'permanent_address_line1','permanent_address_line2','permanent_city','permanent_pincode','permanent_phone'),
            }),
            ('TC Details', {
                'fields': ('tc_no', 'tc_date','medium_of_instruction')
            }),
            ('+1 Details', {
                'fields': ('reg_no', 'month_and_year_of_passing','percentage_of_marks','board','name_of_institution'
                )
            }),
            ('+1 Marks', {
                'fields': ('language', 'english','maths','physics','chemistry','biology','eligible_percentage'
                )
            }),
            ('+2 Details', {
                'fields': ('reg_no1', 'month_and_year_of_passing1','percentage_of_marks1','board1','name_of_institution1'
                )
            }),
            ('+2 Marks', {
                'fields': ('language1', 'english1','maths1','physics1','chemistry1','biology1','eligible_percentage1'
                )
            }),
            ('Enquiry Status', {
                'fields': ('has_enquired',)
            }),
        )


admin.site.register(Department, PersonAdmin)
admin.site.register(OnlineApplication, AdmissionAdmin)
admin.site.register(Achievement,MeasurementMethodAdmin)
admin.site.register(best_moments,MeasurementMethodAdmin)
admin.site.register(Awards,MeasurementMethodAdmin)
admin.site.register(HOD,MeasurementMethodAdmin)
admin.site.register(Professor,MeasurementMethodAdmin)
admin.site.register(Facility,MeasurementMethodAdmin)
admin.site.register(Hyperlink,MeasurementMethodAdmin)
admin.site.register(Gallery,MeasurementMethodAdmin)
admin.site.register(Main_facility,FacilityAdmin) 

