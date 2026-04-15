from django.shortcuts import render
from .forms import ContactForm  # remplace par le vrai nom de ton formulaire

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            
    else:
        form = ContactForm()

    return render(request, 'formulaire/Charlyne html.html', {'form': form})
