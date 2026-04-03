import joblib
import numpy as np



# src/decision_engine.py

def assign_segment(recency, frequency, monetary):
    """
    Assign customer segment based on RFM values
    """

    if monetary > 1000 and frequency > 5:
        return "High Value"
    elif frequency > 5:
        return "Loyal"
    elif recency > 90:
        return "At Risk"
    else:
        return "Low Value"


def get_action(churn_prob, segment):
    """
    Decide action based on churn probability and segment
    """

    if churn_prob > 0.7 and segment == "High Value":
        return "Give 20% discount"
    
    elif churn_prob > 0.7 and segment == "Loyal":
        return "Send personalized offer"
    
    elif churn_prob > 0.7:
        return "Send reminder email"
    
    elif segment == "High Value":
        return "Provide loyalty rewards"
    
    else:
        return "No action"


def make_decision(recency, frequency, monetary, churn_prob):
    """
    Full pipeline: segment + action
    """

    segment = assign_segment(recency, frequency, monetary)
    action = get_action(churn_prob, segment)

    return {
        "segment": segment,
        "action": action
    }

# Load model once
model = joblib.load("models/churn_model.pkl")


def predict_customer(recency, frequency, monetary):
    """
    Predict churn + return business decision
    """

    X = np.array([[recency, frequency, monetary]])

    churn_prob = model.predict_proba(X)[0][1]

    decision = make_decision(recency, frequency, monetary, churn_prob)

    return {
        "churn_probability": float(churn_prob),
        "segment": decision["segment"],
        "action": decision["action"]
    }

