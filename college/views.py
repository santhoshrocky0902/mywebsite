from django.shortcuts import render
from .models import New, Event,Department,HOD,Main_facility, Admission, PersonalInformation,ParentsInformation,StudentDetails,ParentsDetails,TcDetails,EleventhDetails,TwelthDetails,MarkDetails, EnquiryStatus
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
        dob = request.POST['ap_dob_date']
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


        ins = Admission(degree = degree, image=doc_name ,course_type=course_type, year= year, branch = branch)
        ins2 = PersonalInformation(        applicant_name = name, date_of_birth=dob,age=age, blood_group=blood, mother_tounge=mother_tounge, religion = religion, cast=cast, community= community, reserved_category= reserved,physically_handicapped=handicap)
        ins3=ParentsInformation(father_name=fname, father_income= fincome, father_occupation= foccupation,mother_income=mincome, mother_name=mname,mother_occupation=moccupation, gaurdian_income=gincome, gaurdian_name=gname, gaurdian_occupation=goccupation,)
        ins.save()
        ins2.save()
        ins3.save()
        print('saved')
        return render(request, 'thankyou.html')

    else:
        print('not saved')
        print(request.method)
    return render(request, 'admission.html',{'form':form})






    