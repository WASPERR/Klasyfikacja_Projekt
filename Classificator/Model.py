import pickle
import os
from django.conf import settings

model_path = os.path.join(settings.BASE_DIR, 'Classificator_app', 'model', 'Model.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)