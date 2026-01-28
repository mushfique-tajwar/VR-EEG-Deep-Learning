import numpy as np

def get_recommendation(predicted_emotion):
    """
    Recommends an activity based on the classified EEG emotion.
    """
    recommendations = {
        "Scared": {
            "target": "Calm",
            "suggestions": [
                "Practice 4-7-8 deep breathing exercises.",
                "Listen to low-frequency ambient sounds or nature recordings.",
                "Lower the brightness of your VR headset or take a 5-minute 'grounding' break."
            ]
        },
        "Bored": {
            "target": "Happy",
            "suggestions": [
                "Switch to a high-intensity rhythm game (like Beat Saber).",
                "Try a social VR room to interact with other users.",
                "Explore a new, vibrant environment with high visual contrast."
            ]
        },
        "Calm": {
            "target": "Calm",
            "suggestions": ["You are in a great state for meditation or creative building."]
        },
        "Happy": {
            "target": "Happy",
            "suggestions": ["Enjoy the moment! This is the peak experience for this content."]
        }
    }
    
    res = recommendations.get(predicted_emotion, "No recommendation available.")
    return res

# Example Workflow based on your Notebook
# 1. Capture raw EEG (RAW_TP9, RAW_AF7, RAW_AF8, RAW_TP10)
# 2. Preprocess using your RobustScaler
# 3. Predict using one of your models (e.g., 'Transformer' or 'CNN-BiLSTM')

# Mock prediction result for demonstration
current_emotion = "Scared" 
advice = get_recommendation(current_emotion)

print(f"Detected Emotion: {current_emotion}")
print(f"Goal: Shift to {advice['target']}")
print("Recommendations:")
for item in advice['suggestions']:
    print(f"- {item}")