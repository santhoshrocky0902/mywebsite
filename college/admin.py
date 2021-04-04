from django.contrib import admin
from django.forms import TextInput, Textarea
import nested_admin

from .models import New,Event,Department,Achievement,best_moments,Awards,HOD,Professor,Facility,Gallery, Main_facility, Admission, Hyperlink, PaperPublication, PersonalInformation,ParentsInformation,StudentDetails,ParentsDetails,TcDetails,EleventhDetails,TwelthDetails,MarkDetails, EnquiryStatus

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

class PersonalInformationInline(nested_admin.NestedStackedInline):
    model = PersonalInformation
    extra = 1
    def has_add_permission(self, request, obj=None):
        return True

class ParentsInformationInline(nested_admin.NestedStackedInline):
    model = ParentsInformation
    extra = 1
    def has_add_permission(self, request, obj=None):
        return True

class StudentDetailsInline(nested_admin.NestedStackedInline):
    model = StudentDetails
    extra = 1
    def has_add_permission(self, request, obj=None):
        return True

class ParentsDetailsInline(nested_admin.NestedStackedInline):
    model = ParentsDetails
    extra = 1
    def has_add_permission(self, request, obj=None):
        return True

class TcDetailsInline(nested_admin.NestedStackedInline):
    model = TcDetails
    extra = 1
    def has_add_permission(self, request, obj=None):
        return True

class MarkDetailsInline(nested_admin.NestedStackedInline):
    model = MarkDetails
    extra = 1
    exclude = ['another_name', 'some_name']
    def has_add_permission(self, request, obj=None):
        return True

class EnquiryStatusInline(nested_admin.NestedStackedInline):
    model = EnquiryStatus
    extra = 1
    def has_add_permission(self, request, obj=None):
        return True

class EleventhDetailsInline(nested_admin.NestedTabularInline):
    model = EleventhDetails
    inlines = [MarkDetailsInline]
    extra = 1
    def has_add_permission(self, request, obj=None):
        return True

class TwelthDetailsInline(nested_admin.NestedTabularInline):
    model = TwelthDetails
    extra = 1
    inlines = [MarkDetailsInline]
    def has_add_permission(self, request, obj=None):
        return True





class PersonAdmin(admin.ModelAdmin):
    list_display=['get_Name_display']
    inlines = [AchievementInline,BestMomentInline,AwardsInline,HODInline,ProfessorInline,FacilityInline,GalleryInline, PaperPublicationInline]

class FacilityAdmin(admin.ModelAdmin):
    list_display=['get_Name_display']
    inlines = [HyperlinkInline]

class AdmissionAdmin(nested_admin.NestedModelAdmin):
    inlines = [PersonalInformationInline,
    ParentsInformationInline,
    StudentDetailsInline,
    ParentsDetailsInline,
    TcDetailsInline,
    EleventhDetailsInline,
    TwelthDetailsInline,
    EnquiryStatusInline
    ]


admin.site.register(Department, PersonAdmin)
admin.site.register(Admission, AdmissionAdmin)
admin.site.register(Achievement,MeasurementMethodAdmin)
admin.site.register(best_moments,MeasurementMethodAdmin)
admin.site.register(Awards,MeasurementMethodAdmin)
admin.site.register(HOD,MeasurementMethodAdmin)
admin.site.register(Professor,MeasurementMethodAdmin)
admin.site.register(Facility,MeasurementMethodAdmin)
admin.site.register(Hyperlink,MeasurementMethodAdmin)
admin.site.register(Gallery,MeasurementMethodAdmin)
admin.site.register(Main_facility,FacilityAdmin) 

