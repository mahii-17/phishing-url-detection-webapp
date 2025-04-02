import os
from django.shortcuts import render
from .utils import extract_features
import joblib
from django.conf import settings

# Load the model (only once when server starts)
model_path = os.path.join(settings.BASE_DIR, 'detector',
                          'model', 'phishing_model.pkl')
model = joblib.load(model_path)


def home(request):
    result = None
    if request.method == 'POST':
        url = request.POST.get('url')
        features = extract_features(url)
        prediction = model.predict(features)[0]
        result = "Phishing 🚨" if prediction == 1 else "Legit ✅"
    return render(request, 'index.html', {'result': result})
