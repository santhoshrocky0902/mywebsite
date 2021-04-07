from django.shortcuts import render
from MainPage.models import Main_Event
from .forms import ContactForm 
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.generic import View, FormView
from MainPage.forms import SubscriberForm
from django.template import loader
from django.contrib.auth.models import User



# Create your views here.

def thankyou(request):
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
    return render(request, 'thankyou.html', context)

def error_404(request, exception):
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
      
    return render(request, '404.html', {'form':form})


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
        'one': Main_Event.objects.filter(unique_id="1"),
        'two': Main_Event.objects.filter(unique_id="2"),
        'three': Main_Event.objects.filter(unique_id="3"),
        'four': Main_Event.objects.filter(unique_id="4"),
        'five': Main_Event.objects.filter(unique_id="5"),
        'form':form

    }
    return render(request, 'index.html', context)

# about page
def about(request):
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
      
    return render(request, 'about.html', {'form':form})

def president(request):
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
    return render(request, 'president.html', {'form':form})

def founder(request):
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
    return render(request, 'founder.html', {'form':form})

def secratary(request):
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
    return render(request, 'secratary.html', {'form':form})


# contact


def contact(request):
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
    if request.method == 'POST':
        forms = ContactForm(request.POST)
        if forms.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            msg = form.cleaned_data['message']
            sender_mobile = form.cleaned_data['phone']
            message = "{0} has sent you a new message:\n\nEmail:{1}\nPhone:{2}\nMessage:{3}".format(sender_name,sender_email,sender_mobile, msg)
            send_mail('New Enquiry', message, sender_email, ['foodrepo4@gmail.com'])
            return render(request, 'thankyou.html')
    else:
        forms = ContactForm()

    return render(request, 'contact.html',{'forms': forms,'form':form})



# accrediations


def acc1(request):
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
    return render(request, 'acc1.html', {'form':form})


def acc2(request):
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
    return render(request, 'acc2.html', {'form':form})


def acc3(request):
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
    return render(request, 'acc3.html', {'form':form})
