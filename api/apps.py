import os
import joblib
from django.apps import AppConfig
from django.conf import settings
import pandas as pd


class ApiConfig(AppConfig):
    name = 'api'
    model = joblib.load(os.path.join(settings.MODELS, "WeightPredictionLinRegModel.joblib"))