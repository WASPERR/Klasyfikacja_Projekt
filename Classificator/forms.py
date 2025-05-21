from django import forms

class StudentDataForm(forms.Form):
    age = forms.IntegerField(label="Wiek (17-24)", min_value=17, max_value=24)
    gender = forms.ChoiceField(label="Płeć", choices=[(0, 'Kobieta'), (1, 'Mężczyzna')])
    study_hours_per_day = forms.FloatField(label="Godziny nauki dziennie (0-8.3)", min_value=0, max_value=8.3)
    social_media_hours = forms.FloatField(label="Godziny w mediach społecznościowych (0-7.2)",min_value=0, max_value=7.2)
    netflix_hours = forms.FloatField(label="Godziny oglądania Netflixa (0-5.4)", min_value=0, max_value=5.4)
    part_time_job = forms.ChoiceField(label="Praca dorywcza", choices=[(0, 'Nie'), (1, 'Tak')])
    attendance_percentage = forms.FloatField(label="Frekwencja% (56%-100%)", min_value=56, max_value=100)
    sleep_hours = forms.FloatField(label="Godziny snu na dobę (3.2-10)", min_value=3.2, max_value=10)
    diet_quality = forms.ChoiceField(label="Jakość diety", choices=[
        (0, 'Średnia'),
        (1, 'Dobra'),
        (2, 'Słaba')
    ])
    exercise_frequency = forms.ChoiceField(label="Częstotliwość ćwiczeń (razy w tygodniu)", choices=[
        (0, '0'), (1, '1'), (2, '2'),
        (3, '3'), (4, '4'), (5, '5'), (6, '6+')
    ])
    parental_education_level = forms.ChoiceField(label="Wykształcenie rodziców", choices=[
        (0, 'Licencjat'),
        (1, 'Szkoła średnia'),
        (2, 'Magister')
    ])
    mental_health_rating = forms.FloatField(
        label="Ocena zdrowia psychicznego (1-10)",
        min_value=1,
        max_value=10
    )
    extracurricular_participation = forms.ChoiceField(
        label="Uczestnictwo w zajęciach pozalekcyjnych",
        choices=[(0, 'Nie'), (1, 'Tak')]
    )