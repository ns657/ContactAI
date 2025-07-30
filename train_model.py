from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# Sample training data
texts = [
    "I love your website!", "Your service is bad", "Please call me", 
    "You suck", "I need help", "This is amazing", 
    "Why is this so slow?", "Thanks for the info", "Stupid service"
]
labels = [
    "Feedback", "Complaint", "General Inquiry", "Spam", 
    "General Inquiry", "Feedback", "Complaint", "Feedback", "Spam"
]

# Train the model
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(texts, labels)

# Save the model
joblib.dump(model, 'classifier.joblib')
print("Model saved as classifier.joblib")
