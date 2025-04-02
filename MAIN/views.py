from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def shop(request):
    return render(request, 'shop.html', {'title': 'Shop'})

def pricing(request):
    return render(request, 'pricing.html', {'title': 'Pricing'})

def about(request):
    return render(request, 'about.html', {'title': 'About'})

def contact(request):
    return render(request, 'contact.html', {'title': 'Contact'})

def success(request):
    return render(request, 'success.html')



from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construct email content
            subject = f"New message from {name} via OnTap Contact Form"
            message_body = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"

            # Send the email
            send_mail(
                subject,
                message_body,
                email,  # from email
                ['youremail@example.com'],  # your destination email
                fail_silently=False,
            )

            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
