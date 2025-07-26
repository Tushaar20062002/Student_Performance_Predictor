import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt

#loading the train model
model = joblib.load("model.pkl")

#title of the app
st.title("Student Performance Predictor")
st.subheader("Enter the Students details for predict the pass/fail outcome")

#input fields for the user
study_hours = st.slider("Study Hours per Day", 0.0, 10.0, 4.0)
attendance = st.slider("Attendance Percentage", 50, 100, 80)
test_score = st.slider("Avarage Test Score", 0, 100, 60)
sleep_score = st.slider("Sleep Hours per night", 3.0, 10.0, 6.5)
Participations = st.slider("Extracurricular Participation (0-10)", 1, 10, 5)

#prediction button
if st.button("Predict"):
    #converting input data into numpy array
    input_data = np.array([[study_hours, attendance, test_score, sleep_score, Participations]])

    #making prediction
    prediction = model.predict(input_data)[0]

    #showing the result
    if prediction == 1:
        st.success("The student is likely to Pass!")
    else :
        st.error("The student is likely to Fail! Need some improvement.")

#personlize suggesion
st.subheader("Personalized Suggestions")
suggestions = []
if study_hours < 3:
    suggestions.append("Increase your study hours (3+ hours recommended).")
if attendance < 75:
    suggestions.append("Improve your attendance.")
if test_score < 50:
    suggestions.append("Focus on improving your test scores.")
if sleep_score < 6:
    suggestions.append("Get more sleep for better memory")
if Participations < 3:
    suggestions.append("Participate in more extracurricular activities to enhance skills.")

if suggestions:
    for s in suggestions:
        st.write(f"- {s}")
else:
    st.markdown("Great job! You're doing well in all key areas.")

#radar chart for visualizing input data
st.subheader("perfomance chart")
catagories = ['Study Hours', 'Attendance', 'Test Score', 'Sleep Score', 'Participations']
values = [study_hours, attendance/10, test_score/10, sleep_score, Participations]

#closing the loop
values += values[:1]
angles = np.linspace(0, 2 * np.pi, len(catagories), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
ax.plot(angles, values ,color='blue', linewidth=2, linestyle='solid')
ax.fill(angles, values, color='skyblue', alpha=0.4)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(catagories)
ax.set_yticklabels([])
ax.set_title("Student Performance Profile")
st.pyplot(fig)

