from django.urls import path
from . import views

urlpatterns = [
    path('hospital/', views.index, name = "hospital_home_page" ),
    path('hospital/news', views.news, name = "news" ),
    #  facilities
    path('hospital/facilities',views.facility, name = "hospital_facility_page"),
    path('hospital/facilities/24*7',views.service, name = "hf_service"),
    path('hospital/facilities/ambulance',views.ambulance, name = "hf_ambulance"),
    path('hospital/facilities/bloodbank',views.bloodbank, name = "hf_blood"),
    path('hospital/facilities/clinical-material',views.clinical, name = "hf_clinical"),
    path('hospital/facilities/citizen-charter',views.citizen, name = "hf_citizen"),
    path('hospital/facilities/covid-19',views.covid, name = "hf_covid"),
    path('hospital/facilities/ICU',views.icu, name = "hf_icu"),
    path('hospital/facilities/IP&OP',views.ip, name = "hf_ip"),
    path('hospital/facilities/pharmacy',views.pharmacy, name = "hf_pharmacy"),

    # giving

    path('hospital/giving/blood-donate',views.blood_donate, name = "hg_donate"),
    path('hospital/giving/donate-organs',views.organ, name = "hg_organ"),
    path('hospital/giving/pledge-your-eyes',views.eye, name = "hg_eyes"),

    # gallery
    path('hospital/gallery', views.hs_gallery, name = "gallery" ),

    # clinical

    path('hospital/clinical/anaesthiology',views.anaesthiology, name = "hc_anaesthiology"),
    path('hospital/clinical/dentistry',views.dentistry, name = "hc_dentistry"),
    path('hospital/clinical/dermatology',views.dermatology, name = "hc_dermatology"),
    path('hospital/clinical/general-medicine',views.generalmedicine, name = "hc_generalmedicine"),
    path('hospital/clinical/general-surgery',views.generalsurgery, name = "hc_generalsurgery"),
    path('hospital/clinical/OBG',views.obg, name = "hc_obg"),
    path('hospital/clinical/physiotherapy',views.physiotherapy, name = "hc_physiotherapy"),    path('hospital/clinical/anaesthiology',views.anaesthiology, name = "hc_anaesthiology"),
    path('hospital/clinical/radio-diagnosis',views.radiodiagonisis, name = "hc_radiodiagnosis"),
    path('hospital/clinical/ENT',views.ent, name = "hc_ent"),
    path('hospital/clinical/ophthalmology',views.ophthalmology, name = "hc_ophthalmology"),
    path('hospital/clinical/orthopaedics',views.orthopaedics, name = "hc_orthopaedics"),
    path('hospital/clinical/paediatrics',views.paediatrics, name = "hc_paediatrics"),
    path('hospital/clinical/psychiatry',views.psychiatry, name = "hc_psychiatry"),
    path('hospital/clinical/Pulmonology',views.respiratory, name = "hc_respiratory"),

    # super speciality

    path('hospital/super-speciality/cardiology',views.cardiology, name = "hs_cardiology"),
    path('hospital/super-speciality/gasteroenterology',views.gasteroenterology, name = "hs_gasteroenterology"),
    path('hospital/super-speciality/nephrology',views.nephrology, name = "hs_nephrology"),
    path('hospital/super-speciality/neurology',views.neurology, name = "hs_neurology"),
    path('hospital/super-speciality/paediatric-surgery',views.paediatric_surgery, name = "hs_paediatric_surgery"),
    path('hospital/super-speciality/plastic',views.plastic, name = "hs_plastic"),
    path('hospital/super-speciality/surgical-gasteroenterology',views.surgicalgas, name = "hs_surgicalgas"),
    path('hospital/super-speciality/surgical-oncology',views.surgicaloncology, name = "hs_surgicaloncology"),
    path('hospital/super-speciality/urology',views.urology, name = "hs_urology"),
    path('hospital/super-speciality/vascular-surgery',views.vascular_surgery, name = "hs_vascular_surgery"),







    
    
]
