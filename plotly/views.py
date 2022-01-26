from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd

df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"])

def index(request):
    return render(
        request,
        'index.html',
    )

def plot(request):
    return render(
        request,
        'plot.html'
    )

def data(request):
    data = {
        "sepal_length": df["Sepal Length"].to_list(),
        "sepal_width": df["Sepal Width"].to_list(),
        "petal_length": df["Petal Length"].to_list(),
        "petal_width": df["Petal Width"].to_list(),
        "class": df["Class"].to_list()
    }
    return JsonResponse(data)
