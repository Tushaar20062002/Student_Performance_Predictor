# 🎓 Student Performance Predictor

> A smart ML-powered web app that predicts whether a student will **pass or fail** based on real-world academic behavior and gives **personalized improvement suggestions**.

![App Screenshot](https://img.shields.io/badge/Streamlit-Deployed-green?style=flat-square)  
📍 **Live Demo**: [Click to Try the App](https://student-performance-predictor.streamlit.app)  
📁 **Dataset**: `student_data.csv` (Synthetic, 500 entries)  
🧠 **Tech Stack**: Python, Streamlit, Scikit-learn, Matplotlib

---

## 🔍 What This App Does

This project predicts student performance based on 5 key factors:

- 📚 Study Hours  
- 🏫 Attendance  
- 📝 Test Score  
- 😴 Sleep Hours  
- 🙋 Class Participation

### ✨ Features:
- 🔮 ML Prediction (Pass/Fail)
- ✅ Personalized Improvement Suggestions
- 📊 Interactive Radar Chart of Student Profile
- 💡 Clean, Responsive Web UI (Streamlit)
- 🚀 Free Deployment (Live App)

---

## 📂 Project Structure

```bash
Student_Perfomance_Predictor/
│
├── app.py               # Streamlit Web App
├── train_model.py       # ML Model training script
├── model.pkl            # Trained Random Forest Model
├── student_data.csv     # Dataset used for training
├── requirements.txt     # Libraries for deployment
└── README.md            # This file
