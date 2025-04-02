import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Feature extractor


def extract_features(url):
    return [
        len(url),                      # URL Length
        1 if '@' in url else 0,        # Has @
        url.count('.'),                # Number of dots
        1 if url.startswith("https") else 0  # Uses HTTPS
    ]


# Load dataset
df = pd.read_csv("sample_dataset.csv")

# Extract features
X = df['URL'].apply(extract_features).tolist()
y = df['Label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "phishing_model.pkl")

print("✅ Model trained and saved as phishing_model.pkl")
