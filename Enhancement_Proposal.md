# Enhancement Proposal: AI-Based Complaint Classification and Priority Prediction

## Problem Statement
Officers currently see complaints in the order they arrive. A small issue and a serious one look the same in the list. For example, a faded road sign and a collapsed wall both appear as a "new complaint".

The category of a complaint also depends on what the citizen picks. If the citizen picks the wrong one, the complaint can reach the wrong place.

## Proposed Enhancement
When a citizen submits a complaint, the system reads the description and does two things automatically:

1. **Category prediction.** It predicts the type of issue: pothole, garbage, water leak, drainage, streetlight, sanitation, illegal dumping, or property damage.
2. **Priority prediction.** It predicts how urgent the issue is: High, Medium, or Low.

Both predictions are saved with the complaint, along with a confidence score that shows how sure the model is. The Officer Dashboard shows the most urgent complaints first, instead of the oldest first.

## Approach and Tech Choice
- I convert the complaint text into numbers using **TF-IDF**. It gives more weight to important words like "pothole" or "flooding" and less weight to common words like "the".
- I use **Logistic Regression** to predict the category and the priority from those numbers. I train two separate models, one for each task.
- I use scikit-learn to train the models and joblib to save them.
- I chose Logistic Regression because my data is short text, it trains in seconds, and I can see which words led to a prediction. This makes the results easy to check and explain.

## Training Data
I created a labeled dataset from sentence templates, covering all 8 categories and 3 priority levels. It is stored at `backend/ML/data/complaints_dataset.csv`. Each row has the complaint text, its category, and its priority. The size of the dataset can be changed in one place.

## Design Decision: Text Over Images
Citizens upload photos, so image classification was an option. I did not choose it for these reasons:

- A good image model needs thousands of labeled photos for each category, and I do not have such a dataset for civic complaints.
- I can create and label text data myself.
- If I add voice complaints later, the speech will be converted to text first. That text can use the same model with no changes.

## Integration with the Application
- I train the models by running `backend/ML/train.py` during every deploy. The trained model files are not stored in Git, because Git is for code and not for generated files.
- `ml_service.py` loads the trained models when the server starts and provides one function: `predict(text)`.
- When a complaint is submitted, the application calls this function automatically. The citizen and the officer do nothing extra.
- I added three columns to the Complaint table: `predicted_category`, `priority`, and `confidence_score`.

## Testing
- One test checks that the model loads and returns the expected fields, with a confidence score between 0 and 1.
- One test checks that a submitted complaint gets its prediction saved. In this test I replace the model with a fake one, so the test checks only my own code.

## Future Scope
- **Duplicate detection:** If two citizens report the same issue, the system can compare the text and the GPS location of nearby complaints and flag them as likely duplicates. It will reuse the text-to-numbers step I already built.
- **Voice complaints:** A citizen speaks, the speech is converted to text, and the text goes through the same flow as a typed complaint. The ML part needs no changes.