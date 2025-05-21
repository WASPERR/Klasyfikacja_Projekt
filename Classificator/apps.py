from django.apps import AppConfig
import os
import pickle
from django.conf import settings


class ClassificatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Classificator'
    def ready(self):
        model_path = os.path.join(settings.BASE_DIR, 'Classificator', 'model', 'Model')
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
