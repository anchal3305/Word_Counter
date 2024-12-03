from collections import Counter
from django.shortcuts import render

def home(request):
    result = None
    if request.method == "POST":
        text = request.POST.get('text', '')
        words = text.split()
        total_words = len(words)
        word_frequency = Counter(words)

        # Prepare result to be displayed in the template
        result = {
            'text': text,
            'total_words': total_words,
            'word_frequency': dict(word_frequency),
        }
    
    return render(request, 'word_counter_project/index.html', {'result': result})

