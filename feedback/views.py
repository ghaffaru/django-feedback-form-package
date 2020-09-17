from django.shortcuts import render
from .forms import  FeedbackForm
# Create your views here.
def feedback(request):

    if request.method == 'POST':
        pass
    form = FeedbackForm()
    return render(request, 'feedback/index.html', {'form': form})