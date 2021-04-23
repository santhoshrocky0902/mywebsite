
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve 
from django.urls import re_path
from college.views import admission
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "home_page" ),

    # about page
    path('about/', views.about, name = "about_page" ),
    path('about/President', views.president, name = "president" ),
    path('about/Founder', views.founder, name = "founder" ),
    path('about/Secratary', views.secratary, name = "secratary" ),

    # base navigator
    path('', include(('college.urls', 'college'), namespace='college')),
    path('', include(('hospital.urls', 'hospital'), namespace='hospital')),

    # contact us
    path('contact-us/', views.contact, name = "contact-us" ),

    #admission
    path('admission/', admission, name = "admission" ),

    # accrediations

    path('NABH-ACCREDITATION/', views.nabh, name = "acc1" ),
    path('NABL-ACCREDITATION/', views.acc2, name = "acc2" ),
    path('ISO-ACCREDITATION/', views.acc3, name = "acc3" ),
    path('NAAC-ACCREDITATION/', views.acc4, name = "acc4" ),



    
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
handler404 = 'ACS.views.error_404'
# urlpatterns += [
#   re_path(r'^static/(?:.*)$', serve, {'document_root': settings.STATIC_ROOT, })
# ]