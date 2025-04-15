"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import ContactForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name'] 
            phone = form.cleaned_data['phone'] 
            email = form.cleaned_data['email'] 
            content = form.cleaned_data['content'] 

            html = render_to_string('app/email.html',{
                'name': name,
                'email': email,
                'phone': phone,
                'content': content
                })

            send_mail('The contact form subject', 'This is the message', 'noreply@techwithadelle.com', ['adelle_king@outlook.com',], html_message=html),
        else:
            pass
    else:
        form = ContactForm()

    return render(
        request,
        'app/index.html',        
        {
            'form':form,
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


