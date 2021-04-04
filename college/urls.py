from django.urls import path
from . import views

urlpatterns = [
    path('college/', views.index, name = "college_home_page" ),
    path('mci/', views.mcic, name = "mci" ),
    path('college/news', views.news, name = "news" ),

    #  facilities
    path('college/facilities',views.facility, name = "college_facility_page"),
    path('college/facilities/centralab',views.centralab, name = "cf_central_lab"),
    path('college/facilities/library',views.library, name = "cf_library"),
    path('college/facilities/infrastructure',views.infrastructure, name = "cf_infrastructure"),
    path('college/facilities/internet-section',views.internetsection, name = "cf_internet_sec"),
    path('college/facilities/seminar',views.seminar, name = "cf_seminar"),
    path('college/facilities/canteen',views.canteen, name = "cf_canteen"),
    path('college/facilities/hostel',views.hostel, name = "cf_hostel"),
    path('college/facilities/transport',views.transport, name = "cf_transport"),
    path('college/facilities/anti-ragging',views.anti, name = "cf_anti"),
    
    #  departments
    path('college/department/physiology',views.physiology, name ="physiology"),
    path('college/department/anatomy',views.anatomy, name ="anatomy"),
    path('college/department/community-medicine',views.cm, name ="cm"),
    path('college/department/Tb&Chest-Diseases',views.tb, name ="tb"),
    path('college/department/paediatrics',views.Paediatrics, name ="paediatrics"),
    path('college/department/orthopaedics',views.Orthopaedics, name ="orthopaedics"),
    path('college/department/opthalmology',views.Opthalmology, name ="opthalmology"),
    path('college/department/psychiatry',views.Psychiatry, name ="psychiatry"),
    path('college/department/obstetrics',views.Obstetrics, name ="obstetrics"),
    path('college/department/general-surgery',views.gs, name ="gs"),
    path('college/department/forensic-medicine',views.fm, name ="fm"),
    path('college/department/ENT',views.ent, name ="ent"),
    path('college/department/dermatology',views.Dermatology, name ="dermatology"),
    path('college/department/dentistry',views.Dentistry, name ="dentistry"),
    path('college/department/anaesthesiology',views.Anaesthesiology, name ="anaesthesiology"),
    path('college/department/pharmacology',views.Pharmacology, name ="pharmacology"),
    path('college/department/bio-chemistry',views.bc, name ="bc"),
    path('college/department/pathology',views.Pathology, name ="pathology"),
    path('college/department/micro-biology',views.mb, name ="mb"),
    path('college/department/radio-diagnosis',views.rd, name ="rd"),
    path('college/department/general-medicine',views.gm, name ="gm"),

    # ourgroup
    path('college/ourgp',views.ourgroup, name = "cg_ourgroup"),

    # research
   path('college/research/cme',views.cme, name = "cr_cme"),
   path('college/research/paper',views.paper, name = "cr_paper"),
   path('college/research/researchproj',views.researchproj, name = "cr_research_project"),
   path('college/research/conf',views.conf, name = "cr_conference"),
   path('college/research/awards',views.awards, name = "cr_awards"),
 ]
