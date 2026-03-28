import pickle
import pandas as pd

# Load trained model
with open("models/best_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load encoders
with open("models/encoders.pkl", "rb") as f:
    encoders = pickle.load(f)


def predict_salary(experience, education, job_role, location, skills):
    data = pd.DataFrame([{
        "Experience": experience,
        "Education Level": encoders["Education Level"].transform([education])[0],
        "Job Role": encoders["Job Role"].transform([job_role])[0],
        "Location": encoders["Location"].transform([location])[0],
        "Skills Count": skills
    }])

    prediction = model.predict(data)[0]
    return round(prediction, 2)