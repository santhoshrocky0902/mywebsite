from django.shortcuts import render
from .models import New, Event,indexvideo, gallery, Sspeciality,Main_facility,Clinical
from MainPage.forms import SubscriberForm
from django.template import loader
from django.contrib.auth.models import User
from django.core.mail import send_mail



# Create your views here.
def index(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'news': New.objects.all(),
        'events': Event.objects.all(),
        'video': indexvideo.objects.all()
    }
    return render(request, 'hospital/index.html', context )

def news(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():

        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'news': New.objects.all(),
        'events': Event.objects.all()
    }
    return render(request, 'hospital/news.html', context)



# facilities

def facility(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',
                
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
        context = {
            'form':form

        }
    return render(request, 'hospital/facilities/facilities.html', {'form':form})

def service(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
                'form':form,
                'main': Main_facility.objects.filter(Name="1")

    }
    return render(request, 'hospital/facilities/service.html', context )


def ambulance(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
                'form':form,
                 'main': Main_facility.objects.filter(Name="2")
    }
    return render(request,'hospital/facilities/ambulance.html', context)

def bloodbank(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
                'form':form,
                'main': Main_facility.objects.filter(Name="3")
    }
    return render(request,'hospital/facilities/blood.html',context) 

def clinical(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
                'form':form,
    }
    return render(request,'hospital/facilities/clinical.html',context)  

def ip(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Main_facility.objects.filter(Name="6")
    }
    return render(request,'hospital/facilities/ip.html',context)  


def citizen(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
    }
    return render(request,'hospital/facilities/citizen.html',context)  

def covid(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Main_facility.objects.filter(Name="4")
    }
    return render(request,'hospital/facilities/covid.html',context)                  

def icu(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Main_facility.objects.filter(Name="5")
    }
    return render(request,'hospital/facilities/icu.html',context)   

def pharmacy(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Main_facility.objects.filter(Name="7")
    }
    return render(request,'hospital/facilities/pharmacy.html',context)  

# giving

def blood_donate(request):
     form = SubscriberForm(request.POST or None)
     if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
     context = {
        'form':form,
    }
     return render(request,'hospital/giving/blood_donate.html',context )

def organ(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
    }
    return render(request,'hospital/giving/organ.html',context)

# def hand(request):
#     form = SubscriberForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         sender_email = form.cleaned_data['email']
#         message = ""
#         subject = "Thankyou for Subscribing!"
#         html_message = loader.render_to_string(
#             'email.html',
#             {
#                 'user_name': User.first_name,
#                 'subject':  'Thank you fo',   
#             }
#         )
#         send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
#     context = {
#         'form':form,
#     }
#     return render(request,'hospital/giving/hand.html',context)

def eye(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
    }
    return render(request,'hospital/giving/eyes.html',context)

# gallery

def hs_gallery(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'gallery': gallery.objects.all()
    }
    return render(request,'hospital/gallery.html',context)

# clinical

def anaesthiology(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Clinical.objects.filter(Name="1")
    }
    return render(request,'hospital/clinical/anaesthiology.html',context)

def dentistry(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Clinical.objects.filter(Name="2")
    }
    return render(request,'hospital/clinical/dentistry.html',context)

def dermatology(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Clinical.objects.filter(Name="3")
    }
    return render(request,'hospital/clinical/dermatology.html',context)

def generalmedicine(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main':Clinical.objects.filter(Name="5")
    }
    return render(request,'hospital/clinical/general-medicine.html',context)

def generalsurgery(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Clinical.objects.filter(Name="6")
    }
    return render(request,'hospital/clinical/general-surgery.html',context)

def obg(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Clinical.objects.filter(Name="7")
    }
    return render(request,'hospital/clinical/obg.html',context)

    
def physiotherapy(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Clinical.objects.filter(Name="11")
    }
    return render(request,'hospital/clinical/physiotherapy.html',context)

def radiodiagonisis(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Clinical.objects.filter(Name="13")
    }
    return render(request,'hospital/clinical/radio-diagonisis.html',context)

def ent(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Clinical.objects.filter(Name="4")
    }
    return render(request,'hospital/clinical/ent.html',context)

def ophthalmology(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Clinical.objects.filter(Name="8")
    }
    return render(request,'hospital/clinical/ophthalmology.html',context)

def orthopaedics(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Clinical.objects.filter(Name="9")
    }
    return render(request,'hospital/clinical/orthopaedics.html',context)

def paediatrics(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Clinical.objects.filter(Name="10")
    }
    return render(request,'hospital/clinical/paediatrics.html',context)

def psychiatry(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Clinical.objects.filter(Name="12")
    }
    return render(request,'hospital/clinical/psychiatry.html',context)

def respiratory(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Clinical.objects.filter(Name="14")
    }
    return render(request,'hospital/clinical/respiratory.html',context)

# super speciality

def cardiology(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Sspeciality.objects.filter(Name="1")
    }
    return render(request,'hospital/super/cardiology.html',context)

def gasteroenterology(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Sspeciality.objects.filter(Name="2")
    }
    return render(request,'hospital/super/gasteroenterology.html',context)

def nephrology(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Sspeciality.objects.filter(Name="3")
    }
    return render(request,'hospital/super/nephrology.html',context)

def neurology(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Sspeciality.objects.filter(Name="10")
    }
    return render(request,'hospital/super/neurology.html',context)

def paediatric_surgery(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Sspeciality.objects.filter(Name="5")
    }
    return render(request,'hospital/super/paediatric-surgery.html',context)

def plastic(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Sspeciality.objects.filter(Name="4")
    }
    return render(request,'hospital/super/plastic.html',context)

def surgicalgas(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Sspeciality.objects.filter(Name="6")
    }
    return render(request,'hospital/super/surgicalgas.html',context)

def surgicaloncology(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Sspeciality.objects.filter(Name="7")
    }
    return render(request,'hospital/super/surgicaloncology.html',context)

def urology(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Sspeciality.objects.filter(Name="8")
    }
    return render(request,'hospital/super/urology.html',context)

def vascular_surgery(request):
    form = SubscriberForm(request.POST or None)
    if form.is_valid():
        form.save()
        sender_email = form.cleaned_data['email']
        message = ""
        subject = "Thankyou for Subscribing!"
        html_message = loader.render_to_string(
            'email.html',
            {
                'user_name': User.first_name,
                'subject':  'Thank you fo',   
            }
        )
        send_mail(subject, message, 'foodrepo4@gmail.com', [sender_email], html_message= html_message)
    context = {
        'form':form,
        'main': Sspeciality.objects.filter(Name="9")
    }
    return render(request,'hospital/super/vascular-surgery.html',context)

