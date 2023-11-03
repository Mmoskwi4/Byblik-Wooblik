from .forms import ContactForm
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

def contact_view(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = f"Byblik Wooblik ({cd['name']})"
            message = f"Сообщение от {cd['from_email']}, ({cd['name']})\n {cd['message']}"
            send_mail(subject, message, EMAIL_HOST_USER, ['germandemin2211@gmail.com', 'olgazholobko14101998@gmail.com'])
            sent = True
            return render(request, 'sendemail/success.html')
    else:
        form = ContactForm()
    return render(request, 'sendemail/contact.html', {'form': form, 'sent': sent})

def success_view(request):
    return render(request, 'sendemail/success.html')
