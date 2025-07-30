from django.shortcuts import render, redirect
from .forms import ContactForm
import joblib
import os

# Load ML model once
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'classifier.joblib')
model = joblib.load(MODEL_PATH)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            # Predict with your ML model
            classification = model.predict([instance.message])[0]
            instance.classification = classification  # 👈 save it
            instance.save()

            return render(request, 'success.html', {'classification': classification})

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
def success_view(request):
    classification = request.GET.get('classification', None)
    return render(request, 'contact/success.html', {'classification': classification})
from .models import ContactMessage

def view_submissions(request):
    category = request.GET.get('category')
    if category:
        messages = ContactMessage.objects.filter(classification=category).order_by('-timestamp')
    else:
        messages = ContactMessage.objects.order_by('-timestamp')
    categories = ContactMessage.objects.values_list('classification', flat=True).distinct()
    return render(request, 'contact/submissions.html', {
        'messages': messages,
        'categories': categories,
        'selected': category,
    })
