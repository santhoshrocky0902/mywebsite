from django.shortcuts import render
from .models import New, Event,Department,HOD,Main_facility,OnlineApplication
from MainPage.models import mci
from django.template import loader
from django.contrib.auth.models import User
from django.core.mail import send_mail
from MainPage.forms import SubscriberForm


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
        'events': Event.objects.all()
    }
    return render(request, 'college/index.html',context)


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
    return render(request, 'college/news.html', context)

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
    'form':form,
    'f1': Main_facility.objects.filter(Name="1"),
    'f2': Main_facility.objects.filter(Name="2"),
    'f3': Main_facility.objects.filter(Name="3"),
    'f4': Main_facility.objects.filter(Name="4"),
    'f5': Main_facility.objects.filter(Name="5"),
    'f6': Main_facility.objects.filter(Name="6"),
    'f7': Main_facility.objects.filter(Name="7"),
    'f8': Main_facility.objects.filter(Name="8"),
    'f9': Main_facility.objects.filter(Name="9"),

} 
    return render(request, 'college/facilities/facilities.html',context)
# facilities

def centralab(request):
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
    'lab': Main_facility.objects.filter(Name="1")
}
        
    return render(request,'college/facilities/centralab.html',context)

def library(request):
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
    'lab': Main_facility.objects.filter(Name="2")
}
    return render(request,'college/facilities/library.html',context)

def infrastructure(request):
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
    'lab': Main_facility.objects.filter(Name="3")
}
    return render(request,'college/facilities/infrastructure.html',context) 

def internetsection(request):
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
    'lab': Main_facility.objects.filter(Name="4")
}
    return render(request,'college/facilities/internetsection.html',context)  

def seminar(request):
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
    'lab': Main_facility.objects.filter(Name="5")
}    
    return render(request,'college/facilities/seminar.html',context)  

def canteen(request):
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
    'lab': Main_facility.objects.filter(Name="6")
}  
    return render(request,'college/facilities/canteen.html',context)                  

def hostel(request):
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
    'lab': Main_facility.objects.filter(Name="7")
}   
    return render(request,'college/facilities/hostel.html',context)   

def anti(request):
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
    'lab': Main_facility.objects.filter(Name="9")
}   
    return render(request,'college/facilities/antiragging.html',context)  

def transport(request):
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
    'lab': Main_facility.objects.filter(Name="8")
}   
    return render(request,'college/facilities/transport.html',{'form':form})   

# mci clause 

def mcic(request):
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
        'mci': mci.objects.all()

    }
    return render(request, 'college/mci.html',context)



# Departments

def physiology(request):
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
        'physio': Department.objects.filter(Name="1")

    }
    return render(request,'college/department/physiology.html', context)

def anatomy(request):
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
            'Anatomy': Department.objects.filter(Name="2")
    }
    return render(request,'college/department/anatomy.html', context)

def cm(request):
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
            'Community': Department.objects.filter(Name="3"),
    }
    return render(request,'college/department/cm.html', context)

def tb(request):
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
            'Tb': Department.objects.filter(Name="4"),
    }
    return render(request,'college/department/tb.html', context)

def Paediatrics(request):
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
            'Paediatrics': Department.objects.filter(Name="5"),
    }
    return render(request,'college/department/Paediatrics.html', context)

def Orthopaedics(request):
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
            'Orthopaedics': Department.objects.filter(Name="6"),
    }
    return render(request,'college/department/Orthopaedics.html', context)

def Opthalmology(request):
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
            'Opthalmology': Department.objects.filter(Name="7"),
    }
    return render(request,'college/department/Opthalmology.html', context)

def Psychiatry(request):
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
            'Psychiatry': Department.objects.filter(Name="8"),
    }
    return render(request,'college/department/Psychiatry.html', context)

def Obstetrics(request):
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
            'Obstetrics': Department.objects.filter(Name="9"),

    }
    return render(request,'college/department/Obstetrics.html', context)

def gs(request):
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
            'General': Department.objects.filter(Name="10"),
    }
    return render(request,'college/department/gs.html', context)

def fm(request):
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
            'Forensic': Department.objects.filter(Name="11"),
    }
    return render(request,'college/department/fm.html', context)

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
            'ENT': Department.objects.filter(Name="12"),
    }
    return render(request,'college/department/ent.html', context)

def Dermatology(request):
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
            'Dermatology': Department.objects.filter(Name="13"),
    } 
    return render(request,'college/department/Dermatology.html', context)

def Dentistry(request):
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
             'Dentistry': Department.objects.filter(Name="14"),
    }
    return render(request,'college/department/Dentistry.html', context)


def Anaesthesiology(request):
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
            'Anaesthesiology': Department.objects.filter(Name="15"),

    }
    return render(request,'college/department/Anaesthesiology.html', context)


def Pharmacology(request):
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
                'Pharmacology': Department.objects.filter(Name="16"),
    }
    return render(request,'college/department/Pharmacology.html', context)

def bc(request):
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
            'Bio': Department.objects.filter(Name="17"),
    }
    return render(request,'college/department/bc.html', context)

def Pathology(request):
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
             'Pathology': Department.objects.filter(Name="18"),
    }
    return render(request,'college/department/Pathology.html', context)

def mb(request):
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
            'Micro': Department.objects.filter(Name="19"),
    }
    return render(request,'college/department/mb.html', context)

def rd(request):
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
            'Radio': Department.objects.filter(Name="20"),
    }
    return render(request,'college/department/rd.html', context)

def gm(request):
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
            'Generalm': Department.objects.filter(Name="21"),
    }
    return render(request,'college/department/gm.html', context)

    #ourgroup
def ourgroup(request):
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
       
    return render(request,'college/ourgroup/ourgp.html',{'form':form}) 
    
    #research
def cme(request):
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
       
    return render(request,'college/research/cme.html',{'form':form}) 

def paper(request):
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
       
    return render(request,'college/research/paper.html',{'form':form})

def researchproj(request):
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
    return render(request,'college/research/researchproj.html',context)

def conf(request):
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
    return render(request,'college/research/conf.html',context) 

def awards(request):
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
    return render(request,'college/research/awards.html',context)               


#admission

def admission(request):
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
    if request.method == 'POST' and 'ap_file' in request.FILES:
        doc = request.FILES #returns a dict-like object
        doc_name = doc['ap_file']
        degree = request.POST['ap_ugselect']
        # picture = request.POST['ap_file']
        course_type = request.POST['ap_studtype']
        year = request.POST['ap_studyear']
        branch = request.POST['ap_course']
        # personal
        name = request.POST['ap_studname']
        dob = request.POST['ap_dob_date'+'/'+'ap_dob_month'+'/'+'ap_dob_year']
        age = request.POST['ap_dob_age']
        blood = request.POST['ap_blood']
        mother_tounge = request.POST['ap_mothertng']
        religion = request.POST['ap_religion']
        cast = request.POST['ap_cast']
        community = request.POST['ap_community']
        reserved = request.POST['ap_res_category']
        handicap = request.POST.get('ap_handicap','default_value')
        # parents info 
        fname = request.POST['ap_father_name']
        foccupation = request.POST['ap_father_occ']
        fincome = request.POST['ap_father_income']
        mname = request.POST['ap_mother_name']
        moccupation = request.POST['ap_mother_occ']
        mincome = request.POST['ap_mother_inc']
        gname = request.POST['ap_guardian_name']
        goccupation = request.POST['ap_guardian_occ']
        gincome = request.POST['ap_guardian_income']
        # 
        nationality = request.POST['ap_nationality']
        native = request.POST['ap_native']
        state = request.POST['ap_state']
        aphone = request.POST['ap_phone']
        email = request.POST['ap_email']
        address11 = request.POST['ap_address1']
        address12 = request.POST['ap_address2']
        city1 = request.POST['ap_city']
        pincode1 = request.POST['ap_pincode']
        phone1 = request.POST['ap_phone2']
        address21 = request.POST['ap_address_1']
        address22 = request.POST['ap_address_2']
        city2 = request.POST['ap_city_2']
        pincode2 = request.POST['ap_pincode_2']
        phone2 = request.POST['ap_phone_3']
        if 'ap1_xinter_yearpass' in request.POST:
            month_and_year_of_passing = request.POST['ap1_xinter_yearpass']
        else:
            month_and_year_of_passing = False
        if 'ap1_xinter_percent' and 'ap1_xinter_class'and 'ap1_xinter_school' in request.POST:
            percentage_of_marks = request.POST['ap1_xinter_percent']
            board = request.POST['ap1_xinter_class']
            name_of_institution = request.POST['ap1_xinter_school']
        else:
            percentage_of_marks = False
            board= False
            name_of_institution = False
# 
        tc_no = request.POST['ap_tc_no']
        tc_date = request.POST['ap_tc_date'+'/'+'ap_tc_month'+'/'+'ap_tc_year']
        medium_of_instruction = request.POST['ap_medium']
        reg_no = request.POST['ap_reg_no']
        # month_and_year_of_passing = request.POST['ap1_xinter_yearpass']
        # percentage_of_marks = request.POST['ap1_xinter_percent']
        language = request.POST['ap_hsc_marks_ob_lan']
        english = request.POST['ap_hsc_marks_ob_eng']
        maths = request.POST['ap_hsc_marks_ob_math']
        physics = request.POST['ap_hsc_marks_ob_phy']
        chemistry = request.POST['ap_hsc_marks_ob_che']
        biology = request.POST['ap_hsc_marks_ob_bio']
        eligible_percentage = request.POST['ap_elig_percentage']
       
        reg_no1 = request.POST['ap_reg_no12']
        month_and_year_of_passing1 = request.POST['ap2_xinter_yearpass']
        percentage_of_marks1 = request.POST['ap2_xinter_percent']
        board1 = request.POST['ap2_xinter_class']
        name_of_institution1 = request.POST['ap2_xinter_school']
        language1 = request.POST['ap_hsc_marks_ob_lan2']
        english1 = request.POST['ap_hsc_marks_ob_eng2']
        maths1 = request.POST['ap_hsc_marks_ob_math2']
        physics1 = request.POST['ap_hsc_marks_ob_phy2']
        chemistry1 = request.POST['ap_hsc_marks_ob_che2']
        biology1 = request.POST['ap_hsc_marks_ob_bio2']
        eligible_percentage1 = request.POST['ap_elig_percentage2']
        
      

        ins = OnlineApplication(degree = degree, image=doc_name ,course_type=course_type, year= year, branch = branch,
      applicant_name = name, date_of_birth=dob,age=age, blood_group=blood, mother_tounge=mother_tounge, religion = religion, cast=cast, community= community, reserved_category= reserved,physically_handicapped=handicap,
      father_name=fname, father_income= fincome, father_occupation= foccupation,mother_income=mincome, mother_name=mname,mother_occupation=moccupation, gaurdian_income=gincome, gaurdian_name=gname, gaurdian_occupation=goccupation,
      nationality=nationality, native_place=native,state=state,email=email,phone=aphone,current_address_line2=address12,current_city=city1,current_pincode=pincode1,current_phone=phone1,permanent_address_line1=address21, permanent_address_line2=address22,permanent_city=city2,permanent_pincode=pincode2, permanent_phone= phone2,
tc_no=tc_no,tc_date=tc_date,medium_of_instruction=medium_of_instruction,
reg_no=reg_no,month_and_year_of_passing=month_and_year_of_passing,percentage_of_marks=percentage_of_marks,board=board,name_of_institution=name_of_institution,language=language,english=english,maths=maths,physics=physics,chemistry=chemistry,biology=biology,eligible_percentage=eligible_percentage,
reg_no1=reg_no1,month_and_year_of_passing1=month_and_year_of_passing1,percentage_of_marks1=percentage_of_marks1,board1=board1,name_of_institution1=name_of_institution1,language1=language1,english1=english1,maths1=maths1,physics1=physics1,chemistry1=chemistry1,biology1=biology1,eligible_percentage1=eligible_percentage1, 
      )
        ins.save()
        print('saved')

    else:
       pass
    return render(request, 'admission.html',{'form':form})






    