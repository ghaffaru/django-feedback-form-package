from django.shortcuts import render
from .forms import  FeedbackForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def feedback(request):

    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            note = 'Success'
            form.clean()
            # send mail
            send_mail('Website Feedback', 'From ' + form.cleaned_data['name'] + ' with Email: ' + form.cleaned_data['email'] + '\n' + form.cleaned_data['message'],settings.EMAIL_FROM,[settings.EMAIL_TO,])
            form = FeedbackForm()
            return render(request, 'feedback/index.html', {'form': form, 'note': note})
        else:
            return render(request, 'feedback/index.html', {'form': form})
    form = FeedbackForm()
    return render(request, 'feedback/index.html', {'form': form})