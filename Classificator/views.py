from django.shortcuts import render
from .forms import StudentDataForm
import pickle
import os
from django.conf import settings


def index_view(request):
    displayed_prediction = None
    if request.method == 'POST':
        form = StudentDataForm(request.POST)
        if form.is_valid():
            # Wczytujemy model
            model_path = os.path.join(settings.BASE_DIR, 'Classificator/model/Model')
            with open(model_path, 'rb') as f:
                model = pickle.load(f)

            # Dane wejsciowe do predykcji
            features = [
                form.cleaned_data['age'],
                form.cleaned_data['gender'],
                form.cleaned_data['study_hours_per_day'],
                form.cleaned_data['social_media_hours'],
                form.cleaned_data['netflix_hours'],
                form.cleaned_data['part_time_job'],
                form.cleaned_data['attendance_percentage'],
                form.cleaned_data['sleep_hours'],
                form.cleaned_data['diet_quality'],
                form.cleaned_data['exercise_frequency'],
                form.cleaned_data['parental_education_level'],
                form.cleaned_data['mental_health_rating'],
                form.cleaned_data['extracurricular_participation'],
            ]

            # Zinicjalizowanie predykcji
            prediction = model.predict([features])[0]
            # Dodajemy 1 do każdej przewidywanej klasy ponieważ przekazywana klasa 0 to ocena 1 itd.
            displayed_prediction = prediction + 1
    else:
        form = StudentDataForm()

    return render(request, 'Classificator/index.html', {
        'form': form,
        'prediction': displayed_prediction,
    })