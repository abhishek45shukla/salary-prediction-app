# Salary Prediction App

Predicts salary based on a candidate's profile: years of experience, education
level, skill level, communication skills, languages known, technologies
known, tools known, and number of projects completed.

## Deploy Link
https://salary-prediction-app-m8mlbek57wlcphy7xkkttv.streamlit.app/
*(redeploy after updating files — see "Updating the deployed app" below)*

## Tech Stack
- Python
- Streamlit
- Algorithm: Random Forest Regression (upgraded from Linear Regression to
  handle multiple mixed-type features and non-linear interactions between
  them)

## Files
- `New.py` — the Streamlit app (input form + prediction)
- `train_model.py` — builds the training dataset and trains `salary_model.pkl`
- `salary_model.pkl` — the trained scikit-learn pipeline (preprocessing +
  model bundled together)
- `requirements.txt` — dependencies

## About the training data
The original dataset (Kaggle "Salary 2023") only contains years of
experience, so it can't support the new features on its own. `train_model.py`
generates a synthetic dataset that combines all features (experience,
education, skills, communication, languages, tech, tools, projects) with
realistic weightings and random noise, and trains a Random Forest model on
it.

**To use real data instead:** replace `build_synthetic_dataset()` in
`train_model.py` with a `pd.read_csv(...)` of your own labeled data, keeping
the same column names, then rerun `python train_model.py` to regenerate
`salary_model.pkl`.

## Running locally
```bash
pip install -r requirements.txt
streamlit run New.py
```

## Updating the deployed app
Push the updated `New.py`, `salary_model.pkl`, and `requirements.txt` to the
GitHub repo backing the Streamlit Cloud deployment; it will redeploy
automatically.
