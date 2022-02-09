import numpy as np
import pandas as pd
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import os
from django.http import HttpResponse



class WeightPrediction(APIView):
    def post(self, request):
        data = request.data
        height = data['Height']
        gender = data['Gender']
        if gender == 'Male':
            gender = 0
        elif gender == 'Female':
            gender = 1
        else:
            return Response("Gender field is invalid", status=400)
        lin_reg_model = ApiConfig.model
        weight_predicted = lin_reg_model.predict([[gender, height]])[0][0]
        weight_predicted = np.round(weight_predicted, 1)
        response_dict = {"Predicted Weight (kg)": weight_predicted}
        return Response(response_dict, status=200)
    

class ProdRec(APIView):
    def post(self, request):
        df =pd.read_csv(os.path.join(settings.DATA, "data.csv"))
        data = request.data
        inputlat = data['Lat']
        df['dist'] = df['lat'] - inputlat
        results_df = df[df['dist']<=1]
        j = results_df.to_json(orient='records')
        return HttpResponse(j, status=200,content_type = 'application/json')

